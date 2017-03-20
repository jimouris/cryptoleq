#include <stdio.h>
#include <stdio.h>
#include <stdlib.h>

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

// void intersect(int arr1[], int arr2[], int m, int n) {
//      int i = 0, j = 0;
//      loop:
//           if (*arr1 < *arr2) {
//                arr1++; i++;
//           } else if (*arr1 > *arr2) {
//                arr2++; j++;
//           } else {
//                printf("%d\t", *arr1);
//                arr1++; i++;
//                arr2++; j++;
//           }
//      if (i < m && j < n) goto loop;
//      printf("\n");
// }

// int* intersectNoBranch(int arr1[], int arr2[], int m, int n, int*k) {
//      int *res = calloc(m * n, sizeof(int));
//      for (int i = 0; i < m ; i++)
//           for (int j = i ; j < n ; j++)
//                if (arr1[i] == arr2[j]) {
//                     res[(*k)++] = arr1[i];
//                }
//      return res;
// }

int* intersectNoBranch(int arr1[], int arr2[], int m, int n, int* len) {
     int i = 0, j = 0;
     int *res = calloc(m * n, sizeof(int));
     int *resBu = res;
     int *arr2bu = arr2;
     outer:
          j = i;
          arr2 = arr2bu + j;
          inner:
               if (*arr1 != *arr2) goto endif;
                    (*len)++;
                    *res = *arr1;
                    res++;
               endif:
               j++;
               arr2++;
          if (j < n) goto inner;
          i++;
          arr1++;
     if (i < m) goto outer;
     return resBu;
}

int main(void) {
     int arr1[10] = { 1, 5, 9, 10, 12, 13, 16, 18, 20, 25 };
     int arr2[20] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 16, 17, 18, 19, 20, 21, 22, 23, 25 };
     int m = 10, n = 20;

     intersect(arr1, arr2, m, n);

     int k = 0;
     int *res = intersectNoBranch(arr1, arr2, m, n, &k);
     for (int i = 0 ; i < k ; i++) printf("%d\t", res[i]);
     printf("\n");

     return 0;
}
