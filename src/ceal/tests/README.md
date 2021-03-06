<!-- 
* Description of the benchmark 1-2 sentences
* Motivation: why it is selected, what is interesting about it? (1 sentence)
* Its threat model: What value(s) are we protecting exactly (e.g., inputs, outputs, input length, iterations, etc)? What we cannot protect (e.g., input size), or don’t care to protect?
* How the algorithm is converted to privacy preserving version (1 sentence) 
-->

- [x] __[Fibonacci](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/fibonacci)__ [wiki](https://en.wikipedia.org/wiki/Fibonacci_number)
    * The Fibonacci numbers are the numbers in a sequence that is characterized by the fact that every number after the first two is the sum of the two preceding ones.
    * __Threat Model:__ The input number is given encrypted, while we have modified the algorithm in a way to protect the input from information leaked from the computation time.
    * The only arrangement is that the program can compute up to a maximum/fixed number (N). When the user asks for the fib(X), 0 <= x <= N, the program computes every fib in range [0, N] and prints the fib(X). This arrangement was made in order to protect the data from side channel attacks, like leaking information about X from the computation time.


- [x] __[Factorial](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/factorial)__ [wiki](https://en.wikipedia.org/wiki/Factorial)
    * The factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n.
    * __Threat Model:__ Same as Fibonacci.
    

- [x] __[Matrix Multiplication](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/matrixMultiplication)__ [wiki](https://en.wikipedia.org/wiki/Matrix_multiplication)
    * Matrix multiplication is a binary operation that produces a matrix from two matrices. If A is an ```n × m``` matrix and B is an ```m × p``` matrix, their matrix product AB is an ```n × p``` matrix, in which the m entries across a row of A are multiplied with the m entries down a columns of B and summed to produce an entry of AB.
    * __Threat Model:__ In this benchmark, we are protecting the contents of the matrices, we do not care to protect the dimensions (```n m m p```) which are given as open values.
    * The matrix product is a ```n × p``` matrix with encrypted values.


- [x] __[Intersect Arrays/Sets](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/setIntersection)__ [PSI](https://www.cs.virginia.edu/~evans/pubs/ndss2012/psi.pdf)
    * Protocols for private set intersection PSI allow two parties holding sets S and S' to compute the intersection I = S ∩ S' without revealing to the other party any additional information about their respective sets (except their sizes).
    * __Threat Model:__ In this benchmark, we care to protect the contents of the sets. We do not care to protect the size (N) of the biggest set which is given as open value; the smaller array is extended also in size N and filled up with a fixed value.


- [x] __[Insertion-sort](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/insertionSort)__ [wiki](https://en.wikipedia.org/wiki/Insertion_sort)
    * Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. 
    * Performance:
        - Worst-case: О(n^2)
        - Average: О(n^2)
        - Best-case: O(n)
    * __Threat Model:__ In this benchmark, we do not care to protect the size of the array. We are protecting the contents of both the input/unsorted and output/sorted arrays.


- [x] __[Permutations](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/permutations)__ [wiki](https://en.wikipedia.org/wiki/Permutation)
    * The notion of permutation relates to the act of arranging all the members of a set into some sequence or order, or if the set is already ordered, rearranging its elements, a process called permuting. This benchmark, computes all permutations of a given array/set.
    * __Threat Model:__ In this benchmark, we do not care to protect the size of the array. We are protecting the contents of the input, as well as all the output/permuted arrays.


- [x] __[Sieve of Eratosthenes](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/sieveOfEratosthenes)__ [wiki](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
    * In mathematics, the sieve of Eratosthenes, is a simple, ancient algorithm for finding all prime numbers up to any given limit. It does so by iteratively marking as composite (i.e. not prime) the multiples of each prime, starting with the multiples of 2. In this benchmark, we print all prime numbers up to a fixed/maximum number using the sieve of Eratosthenes method.
    * __Threat Model:__ In this benchmark, the only open value will be the maximum number to compute if it is prime. In order to protect both the primes themselves and the number of primes found from 2 to Num, if a number is prime we print the encryption of that prime, else we print the encryption of zero.


- [x] __[Prime Numbers](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/prime_numbers)__ [wiki](https://en.wikipedia.org/wiki/Prime_number)
    * A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. In this benchmark, we find and print all prime numbers from 2 to a fixed/maximum number N. In this benchmark, we use the [Sieve of Eratosthenes](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/sieveOfEratosthenes) in rounds in order to calculate prime numbers without stopping.
    * __Threat Model:__  Same as in the Sieve of Eratosthenes benchmark. 


- [x] __[N-Queens](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/nqueens)__ [wiki](https://en.wikipedia.org/wiki/Eight_queens_puzzle)
    * The 8-queens puzzle is the problem of placing eight chess queens on an 8×8 chessboard so that no two queens threaten each other. Thus, a solution requires that no two queens share the same row, column, or diagonal. The N-Queens problem is the problem of placing N queens on an NxN chessboard.
    * __Threat Model:__ In this benchmark, we do not care to protect the size of the chessboard. What we care to protect is the contents/positions of the placed queens.


- [x] __[Tak function](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/tak_function)__ [wiki](https://en.wikipedia.org/wiki/Tak_(function))
    * In computer science, the Tak function is a recursive function, named after Ikuo Takeuchi. Tak function is a popular recursion performance test.
    * __Threat Model:__ Every variable is encrypted.
``` 
def tak( x, y, z)
  if y < x
    tak(tak(x-1, y, z),
        tak(y-1, z, x),
        tak(z-1, x, y))
  else
    z
end
```


- [x] __[Number Occurrences](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/numOccurrences)__ *(not for benchmarking)*
    * Given an array of integers count the occurrences of a specific number.
    * __Threat Model:__ The input number as well as the array of integers are given encrypted. No information leaked.



*Source: Wikipedia*
