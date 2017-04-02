#include <stdio.h>

/********************************************************
** Create a boolean array "prime[0..n]" and initialize
** all entries it as true. A value in prime[i] will
** finally be false if i is Not a prime, else true.
********************************************************/

#if 1
void sieveOfEratosthenes(int n) {
    int prime[n+1];
    for (int i = 0 ; i < n+1 ; i++) 
        prime[i] = 1;
 
    for (int p = 2 ; p*p < n+1 ; p++) {
        /** This condition "prunes" some iterations, but the algorithm also work without it
         * In cryptoleq, we cannot have jumps(if/else) over encrypted values; and prime[p] is encrypted.
         * if (prime[p])                               // If prime[p] is not changed, then it is a prime 
        **/
        for (int i = 2*p ; i < n+1 ; i += p) {   // Update all multiples of p
            prime[i] = 0;
        }
    }

    for (int p = 2 ; p < n+1 ; p++)                 // Print all prime numbers
        printf("%d ", p * prime[p]);
    printf("\n");
}

#else
/********************************************************
** A low level implementation of the above function
********************************************************/
void sieveOfEratosthenes(int n) {
    int prime[n+1];
    int *p_ptr_bu = prime;
    int i = 0;
    init_loop:
        prime[i] = 1;
        i++;
    if (i != n+1) goto init_loop;

    int x, p = 2;
    int *primeOuter = p_ptr_bu+p;
    int *primeInner;
    outer_loop:
        i = p; i += p;
        inner_loop:
            primeInner = p_ptr_bu + i;
            *primeInner = 0;
            i += p;
        if (i < n+1) goto inner_loop;
        primeOuter++;
        p++;
    if (p*p < n+1) goto outer_loop;

    p = 2;
    print_loop:
        printf("%d ", p * p_ptr_bu[p]);
        p++;
    if (p != n+1) goto print_loop;
    printf("\n");
}
#endif

int main(void) {
    int n = 100;

    sieveOfEratosthenes(n);

    return 0;
}
