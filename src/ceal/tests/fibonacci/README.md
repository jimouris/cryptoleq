### Fibonacci numbers
```F(n) = F(n-1) + F(n-2)```

```0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1587 ...```

##### Concept: 
Given a database with numbers in range [1, 50], calculate the Fibonacci of a specific number.

##### Idea: 
Iterate all the numbers in order to avoid side channel attacks and compute the Fibonacci number for each one. Keep only the result of the requested number and print it in the end.

#### Two Approaches:
- [Unencrypted/Open Numbers](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/fibonacci/fibonacci_o.sca): in order to demonstrate with unencrypted numbers the idea.
- [Encrypted Numbers](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/fibonacci/fibonacci_s.sca):
Given the [db.sec](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/fibonacci/db.sec) (which consists of enc(1) to enc(50)) calculate the Fibonacci of the number given in [input.sec](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/fibonacci/input.sec) (which is 12).
