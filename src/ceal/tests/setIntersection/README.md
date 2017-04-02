### Sorted Array Intersection
Given two arrays of integers ```e.g. 1 1 1 2 3 X X X X X``` and ``` 2 2 2 1 1 1 1 1 1 1``` store and print the intersection of those two arrays ```1  1  1  2  X  X  X  X  X  X```.

**Open values:** The arrays size (given in [header.opn](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/setIntersection/header.opn)). If the sizes of the two arrays are not equal, pad the smaller one with a constant value X (```e.g. 999```).

**Encrypted Values:** The content of the arrays.

**Result:** We want to protect both the contents and the size of the intersection. The only way to do this, is by returning a fixed size array. As already mentioned, the two arrays' lengths must be equal. At start, the array will be initialized with encrypted zeros. In the end, some positions will have the encrypted numbers that were in both arrays, and the others will have encrypted X's.

#### Two Approaches:
- [Unencrypted/Open Numbers](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/setIntersection/setIntersection_o.sca), [db.opn](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/setIntersection/db.opn)
- [Encrypted Numbers](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/setIntersection/setIntersection_s.sca), [db.sec](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/setIntersection/db.sec)

