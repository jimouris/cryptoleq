#include <stdio.h>
#include <stdlib.h>

void swap(int *x, int *y) {
    int tmp = *x;
    *x = *y;
    *y = tmp;
}

#if 0

void printArray(int *array, int size) {
    for (int i = 0 ; i < size ; i++)
        printf("%d", array[i]);
    printf("\n");
}

void permute(int *array, int size, int l, int r) {
    if (l == r) {
        printArray(array, size);
    } else {
        for (int i = l; i <= r; i++) {
            swap((array+l), (array+i)); // swap
            permute(array, size, l+1, r);
            swap((array+l), (array+i)); // restore the swap
        }
    }
}

int main(void) {
    int array[3] = { 1, 2, 3 };
    int n = sizeof(array) / sizeof(int);
    permute(array, n, 0, n-1);
    return 0;
}

#else

int main(void) {
    int *stack = calloc(256, sizeof(int));
    int *stack_bu = stack;
    int stack_ptr = 0;
    int a[3] = { 1, 2, 3 };
    int *array = a;
    int *array_bu = a;
    int *ptr1, *ptr2;
    int size = 3;

    int i, j, rr;
    int l = 0;
    int r = size-1;
recursion:
    if (l != r) goto else_cond;
        j = 0;
        array = array_bu;
        print_loop:
            printf("%d", *array);
            array++;
            j++;
        if (j != size) goto print_loop;
        array = array_bu;
        printf("\n");
        goto recursion_return;
    else_cond:
        i = l;
        permute_loop:
            array = array_bu;
            ptr1 = array + l;
            ptr2 = array + i;
            swap(ptr1, ptr2);     // swap
            
            /* stack variables */
            j = 0;
            stack += stack_ptr;
            stack_loop:
                *stack = *array;
                stack++;
                array++;
                j++;
            if (j != size) goto stack_loop;
            array = array_bu;
            stack = stack_bu;
            stack_ptr += size;

            stack += stack_ptr;
            *stack = l;
            stack++;
            *stack = r;
            stack++;
            *stack = i;
            stack_ptr += 3;
            stack = stack_bu;
            
            l++;
            goto recursion;
recursion_return:

            /* unstack variables */
            stack = stack_bu;
            stack += stack_ptr;
            stack--;
            i = *stack;
            stack--;
            r = *stack;
            stack--;
            l = *stack;
            stack_ptr -= 3;
            stack_ptr -= size;
            j = 0;

            array = array_bu;
            stack = stack_bu;
            stack += stack_ptr;
            unstack_loop:
                *array = *stack;
                stack++;
                array++;
                j++;
            if (j != size) goto unstack_loop;

            ptr1 = array + l;
            ptr2 = array + i;
            swap(ptr1, ptr2); 
            i++;
            rr = r;
            rr++;
        if (i != rr) goto permute_loop;
        if (stack_ptr != 0) goto recursion_return;

    return 0;
}

#endif
