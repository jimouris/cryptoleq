/* insertion sort ascending order */
#include <stdio.h>
 
// swap if the second is greater
void minswp(int *x, int *y) {
    if (*x < *y) {
        int tmp = *x;
        *x = *y;
        *y = tmp;
    }
}

#if 0

int main(void) {
    int n = 10, i, j;
    int array[10] = { 4, 2, 5, 9, 1, 0, 4, 3, 9, 8 };

    for (i = 1 ; i < n; i++) {
        j = i;
        while (j != 0) {
            minswp(&array[j-1], &array[j]);
            j--;
        }
    }

    for (i = 0; i < n; i++)
        printf("%d\t", array[i]);
    printf("\n");
    return 0;
}

#else

int main(void) {
    int n = 10, j;
    int array[10] = { 4, 2, 5, 7, 1, 0, 11, 3, 9, 8 };
    int *arrayPrev = array;
    int *arrayCur = array;

    int i = 1;
    outer_loop:
        j = i;
        arrayCur = array + i;
        inner_loop:
            arrayPrev = arrayCur-1;
            minswp(arrayCur, arrayPrev);
            j--;
            arrayCur--;
        if (j != 0) goto inner_loop;
        i++;
    if (i != n) goto outer_loop;

    for (i = 0; i < n; i++)
        printf("%d\t", array[i]);
    printf("\n");
    return 0;
}

#endif