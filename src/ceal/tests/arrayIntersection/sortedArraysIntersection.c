#include <stdio.h>
#include <stdio.h>
#include <stdlib.h>

/*********************************
** Efficient Array intersection
**********************************/
/**
 * This is the most efficient array intersection algorithm, 
 * but if translated in cryptoleq/CEAL it will have branches on encrypted values.
 *
 * compare a[i] with b[j]:
 * if equal print
 * else inc the smaller index
 **/
void intersect(int arr1[], int arr2[], int m, int n) {
     int i = 0, j = 0;
     while (i < m && j < n) {
          if (arr1[i] < arr2[j]) {
               i++;
          } else if (arr1[i] > arr2[j]) {
               j++;
          } else {
               printf("%d\t", arr1[i++]);
               j++;
          }
     }
     printf("\n");
}


/************************************************************
** Array intersection without Branches on Encrypted values
************************************************************/
#if 1
/**
 * For every element in the first array, check every element in the second
 * Return an array of size M*N, where M is the size of the first array, N of the second,
 * Some values will be the encrypted 0, the others will be the intersection of the two arrays.
 **/
int* intersectNoBranch(int arr1[], int arr2[], int m, int n) {
     int k = 0; 
     int *res = calloc(m * n, sizeof(int));
     for (int i = 0; i < m ; i++) {
          for (int j = i ; j < n ; j++) {
              int eq = (arr1[i] == arr2[j]) ? 1 : 0;
              res[k++] = eq * arr1[i];
          }
     }
     return res;
}
#else
int* intersectNoBranch(int arr1[], int arr2[], int m, int n) {
     int i = 0, j = 0, eq;
     int *res = calloc(m * n, sizeof(int));
     int *resBu = res;
     int *arr2bu = arr2;
     outer:
          j = i;
          arr2 = arr2bu + j;
          inner:
               eq = (*arr1 == *arr2) ? 1 : 0;
               *res = eq * *arr1;
               res++;
               j++;
               arr2++;
          if (j < n) goto inner;
          i++;
          arr1++;
     if (i < m) goto outer;
     return resBu;
}
#endif

int main(void) {
     // int arr1[10] = { 1, 5, 9, 10, 12, 13, 16, 18, 20, 25 };
     int arr1[10] = { 1, 1, 2, 2, 2, 3, 3, 3, 3, 3 };
     int arr2[20] = { 1, 1, 1, 2, 3, 6, 7, 8, 9, 11, 12, 16, 17, 18, 19, 20, 21, 22, 23, 25 };
     int m = 10, n = 20;

     intersect(arr1, arr2, m, n);

     int *res = intersectNoBranch(arr1, arr2, m, n);
     for (int i = 0 ; i < m*n ; i++)
          if (res[i] != 0) printf("%d\t", res[i]);
     printf("\n");

     return 0;
}
