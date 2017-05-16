#include <stdio.h>

#define N 50
#define MAX_N 200
/********************************************************
** Create a boolean array "prime[0..n]" and initialize
** all entries it as true. A value in prime[i] will
** finally be false if i is Not a prime, else true.
********************************************************/

void sieveOfEratosthenes(int *prime, int base) {
    for (int i = 0 ; i < N+1 ; i++) 
        prime[i] = 1;
 
    for (int p = 2 ; p*p < N+1 + base ; p++) {
        
        int i = 2*p;
        while (i < base) i += p;

        for ( ; i < N+1 + base ; i += p) {   // Update all multiples of p
            prime[i - base] = 0;
        }
    }

    for (int p = 0 ; p < N ; p++)              // Print all prime numbers
        printf("%d ", (p+base) * prime[p]);
    printf("\n");
}


int main(void) {
    int prime[N+1];
    int cnt = 0;
    do {
        
        sieveOfEratosthenes(prime, cnt);
        cnt += N;

    } while (cnt < MAX_N);

    return 0;
}
