#include <stdio.h>
#include <stdlib.h>

#define X 9999
#define XX 99999

/************************************************************
** Array intersection without Branches on Encrypted values
*************************************************************
************************************************************************************************
** For every element in the first array, check every element in the second
** Return an array of size min(M, N), where M is the size of the first array, N of the second,
** The values at the beginning of the array will be the intersection of the two arrays, and
** the others will be X padding.
***********************************************************************************************/

#if 0

int* intersect(int arr1[], int arr2[], int m, int n) {
    int k = 0;
    int minlen = (m < n) ? m : n;
    int *res = malloc(minlen * sizeof(int));
    for (int i = 0; i < m ; i++) {
        for (int j = 0 ; j < n ; j++) {
            int eq = (arr1[i] == arr2[j]) ? 1 : 0;
            res[k] = eq * arr1[i];
            k += eq;
            arr2[j] += eq * X;
            arr1[i] += eq * XX;
        }
    }
    for ( ; k < minlen ; k++)
        res[k] = X;
    return res;
}

#else

int* intersect(int arr1[], int arr2[], int m, int n) {
    int i = 0, j = 0, k = 0, eq;
    int minlen = (m < n) ? m : n;
    int *res = malloc(minlen * sizeof(int));
    int *res_bu = res;
    int *arr2bu = arr2;
    outer:
        j = 0;
        arr2 = arr2bu;
        inner:
            eq = (*arr1 == *arr2) ? 1 : 0;
            *res = eq * *arr1;
            res += eq;
            k += eq;
            *arr2 += eq * X;
            *arr1 += eq * XX;
            j++;
            arr2++;
        if (j < n) goto inner;
        i++;
        arr1++;
    if (i < m) goto outer;

    for ( ; k < minlen ; k++, res++)
    *res = X;
    return res_bu;
}

#endif

int main(void) {

#if 1
    int arr1[5] = { 1, 1, 1, 2, 3 };
    int arr2[10] = { 2, 2, 2, 1, 1, 1, 1, 1, 1, 1 };
#else
    int arr1[7] = { 1, 2, 3, 4, 5, 6, 7 };
    int arr2[4] = { 10, 11, 12, 13 };
#endif

    int m = sizeof(arr1) / sizeof(int);
    int n = sizeof(arr2) / sizeof(int);

    int minlen = (m < n) ? m : n;
    int *res = intersect(arr1, arr2, m, n);
    for (int i = 0 ; i < minlen ; i++)
        if (res[i] == X)
            printf("X  ");
        else
            printf("%d  ", res[i]);
    printf("\n");

    return 0;
}
