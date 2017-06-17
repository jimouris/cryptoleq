#define _GNU_SOURCE
#include <ctype.h>
#include <fcntl.h>
#include <sched.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

char** parse(FILE* fp) {
    size_t a_cap = 8;
    char** a = malloc(a_cap * sizeof(char*));
    size_t ai_cap = 16;
    char* ai = malloc(ai_cap * sizeof(char));
    size_t i = 0, j = 0;
    int c;
    while ((c = fgetc(fp)) != '\n' && c != EOF) {
        if (isspace(c)) {
            if (j == 0) continue;
            ai[j] = 0;
            a[i++] = ai;
            if (i + 2 == a_cap) {
                a_cap += a_cap;
                a = realloc(a, a_cap * sizeof(char*));
            }
            ai_cap = 16;
            ai = malloc(ai_cap * sizeof(char));
            j = 0;
        } else {
            ai[j++] = c;
            if (j == ai_cap) {
                ai_cap += ai_cap;
                ai = realloc(ai, ai_cap * sizeof(char));
            }
        }
    }
    if (j) {
        ai[j] = 0;
        a[i++] = ai;
    } else {
        free(ai);
    }
    if (c == EOF && i == 0) {
        free(a);
        return NULL;
    }
    a[i] = NULL;
    return a;
}

char** prepend(char** a, char* ai) {
    size_t i = 0;
    while (a[i] != NULL) ++i;
    do {
        a[i + 1] = a[i];
    } while (i--);
    a[0] = ai;
}

void append(char** a, char* ai) {
    size_t i = 0;
    while (a[i] != NULL) ++i;
    a[i] = ai;
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s [command file] [number of CPUs]\n", argv[0]);
        return EXIT_FAILURE;
    }
    FILE* fp = fopen(argv[1], "r");
    if (fp == NULL) {
        fprintf(stderr, "%s: %s: File not found\n", argv[0], argv[1]);
        return EXIT_FAILURE;
    }
    int cpus = atoi(argv[2]);
    if (cpus <= 0 || cpus > 256) {
        fprintf(stderr, "%s: %d: Invalid number of CPUs\n", argv[0], cpus);
        fclose(fp);
        return EXIT_FAILURE;
    }
    char stats_header[] = "IP watch list { _G_start _omul_start _seq_start _smul_start }";
    pid_t* pids = malloc(cpus * sizeof(pid_t));
    int com = 0;
    char** args;
    while ((args = parse(fp)) != NULL) {
        if (args[0] == NULL) continue;
        int cpu = com++;
        if (com > cpus) {
            int status = EXIT_FAILURE;
            pid_t pid = wait(&status);
            if (pid == -1) {
                fprintf(stderr, "%s: Failed to collect command\n", argv[0]);
                return EXIT_FAILURE;
            }
            if (status != EXIT_SUCCESS) {
                fprintf(stderr, "%s: Received failed status: %d\n", argv[0], status);
                return EXIT_FAILURE;
            }
            cpu = 0;
            while (pids[cpu] != pid) cpu += 1;
            printf("Collected command on CPU %d\n", cpu);
        }
        pids[cpu] = fork();
        if (pids[cpu] == (pid_t) -1) {
            fprintf(stderr, "%s: Failed to create process for command %d\n", argv[0], com);
            return EXIT_FAILURE;
        }
        if (pids[cpu] == 0) {
            cpu_set_t* set = CPU_ALLOC(cpus);
            size_t size = CPU_ALLOC_SIZE(cpus);
            CPU_ZERO_S(size, set);
            CPU_SET_S(cpu, size, set);
            if (sched_setaffinity(getpid(), size, set) == -1) {
                fprintf(stderr, "%s: Command %d failed to set affinity\n", argv[0], com);
                return EXIT_FAILURE;
            }
            CPU_FREE(set);
            char file[256];
            sprintf(file, "%s_out_%d.out", args[1], com);
            int fd = open(file, O_RDWR | O_CREAT, S_IRUSR | S_IWUSR);
            if (fd == -1 || dup2(fd, STDOUT_FILENO) == -1 || close(fd) == -1) {
                fprintf(stderr, "%s: Command %d failed to set output file\n", argv[0], com);
                return EXIT_FAILURE;
            }
            sprintf(file, "%s_err_%d.out", args[1], com);
            fd = open(file, O_RDWR | O_CREAT, S_IRUSR | S_IWUSR);
            if (fd == -1 || dup2(fd, STDERR_FILENO) == -1 || close(fd) == -1) {
                fprintf(stderr, "%s: Command %d failed to set error file\n", argv[0], com);
                return EXIT_FAILURE;
            }
            sprintf(file, "%s_stats_%d.out", args[1], com);
            fd = open(file, O_RDWR | O_CREAT, S_IRUSR | S_IWUSR);
            if (fd == -1) {
                fprintf(stderr, "%s: Command %d failed to set stats file\n", argv[0], com);
                return EXIT_FAILURE;
            }
            write(fd, stats_header, sizeof(stats_header));  
            if (close(fd) == -1) {
                fprintf(stderr, "%s: Command %d failed to close stats file\n", argv[0], com);
                return EXIT_FAILURE;
            }

            prepend(args, "time");
            append(args, "-d");
            append(args, file);

            execvp(args[0], args);
            fprintf(stderr, "%s: Command %d failed to execute\n", argv[0], com);
            return EXIT_FAILURE;
        }
        printf("Executing command %d: \"", com);
        size_t i = 0;
        while (args[i] != NULL) {
            if (i) printf(" ");
            printf("%s", args[i]);
            free(args[i++]);
        }
        printf("\" on CPU %d\n", cpu);
        fflush(stdout);
        free(args);
    }
    fclose(fp);
    int i = 0;
    while (i < com && i < cpus) {
        int status = EXIT_FAILURE;
        pid_t pid = wait(&status);
        if (pid == -1) {
            fprintf(stderr, "%s: Failed to collect command (final)\n", argv[0]);
            return EXIT_FAILURE;
        }
        if (status != EXIT_SUCCESS) {
            fprintf(stderr, "%s: Received failed status: %d\n", argv[0], status);
            return EXIT_FAILURE;
        }
        int cpu = 0;
        while (pids[cpu] != pid) cpu += 1;
        printf("Collected command on CPU %d\n", cpu);
        i += 1;
    }
    printf("Executed %d commands successfully\n", com);
    free(pids);
    return EXIT_SUCCESS;
}
