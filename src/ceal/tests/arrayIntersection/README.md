### Sorted Array Intersection
Given two arrays of integers ```e.g. 1, 5, 9, 10, 12, 13, 16, 18, 20, 25``` and ```1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 16, 17, 18, 19, 20, 21, 22, 23, 25``` store and print the intersection of those two arrays ```1, 5, 9, 12, 16, 18, 20, 25```.

**Open values:** The array sizes (```e.g. m, n``` given in [header.opn](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/arrayIntersection/header.opn)).

**Encrypted Values:** The content of the arrays.

**Result:** We want to protect both the contents and the size of the intersection. The only way to do this, is by returning a fixed size array. If ```m``` is the size of the first array and ```n``` is the size of the second, the result of the intersection will be less or equal than ```m*n```. At start, the array will be initialized with encrypted zeros. In the end, some positions will have the encrypted numbers that were in both arrays, and the others will still have encrypted zeros.

#### Two Approaches:
- [Unencrypted/Open Numbers](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/arrayIntersection/sortedArraysIntersection_o.sca), [db.opn](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/arrayIntersection/db.opn)
- [Encrypted Numbers](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/arrayIntersection/sortedArraysIntersection_s.sca), [db.sec](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/arrayIntersection/db.sec)

