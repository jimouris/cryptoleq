### Matrices Multiplication
Given two arrays of integers e.g.
```
A:
1 2 3
4 5 6
```
and
```
B:
1 2 3 4
4 4 3 2 
9 7 6 4
```
multiply and store those two arrays 
```
AxB:
36 31 27 20
78 70 63 50
```

**Open values:** The array sizes (```e.g. r1 c1 r2 c2```, given in [header.opn](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/matrixMultiplication/header.opn)).

**Encrypted Values:** The content of the two matrices.

**Result:** The only thing we want to protect is the contents of the array. We do not want to protect the size of the result, it would be ```r1 * c2``` which are open values.

#### Two Approaches:
- [Unencrypted/Open Numbers](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/matrixMultiplication/matrix_mult_o.sca) [db.opn](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/matrixMultiplication/db.opn)
- [Encrypted Numbers](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/matrixMultiplication/matrix_mult_s.sca) [db.sec](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/matrixMultiplication/db.sec)

