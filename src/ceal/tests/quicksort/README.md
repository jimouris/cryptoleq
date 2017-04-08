### Quick-Sort
Quicksort is an efficient sorting algorithm, serving as a systematic method for placing the elements of an array in order. This benchmark, sorts and prints the given array.

**Open value:** We cannot protect the size of the input/given array.

**Encrypted Values:** We are protecting the contents of the input, as well as all the output/sorted array.

**Recursion:** Cryptoleq does not have "native" recursion; but it can provide a large amount of memory to simulate recursion. In order to do so, before every recursive call (```goto to the beginning```) we must store all local variables into a stack, and respectively after returning from a recursive call we must unstack the stored local variables.

#### Two Approaches:
- [Unencrypted/Open Numbers](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/quicksort/quicksort_o.sca)
- [Encrypted Numbers](https://github.com/jimouris/cryptoleq/tree/master/src/ceal/tests/quicksort/quicksort_s.sca)

##### Stack-based quicksort C-code:
```
int partition(int *arr, int l, int r) {
    int pivot = arr[l];
    int i = l;
    int p = r + 1;
    while (1) {
        do ++i; while (arr[i] <= pivot && i <= r);
        do --p; while (arr[p] > pivot);
        if (i >= p) break;
        swap(&arr[i], &arr[p]);
    }
    swap(&arr[l], &arr[p]);
    return p;
}
```
```
void quickSort(int *arr, int l, int r) {
    int stack[r - l + 1];
    int stack_ptr = 0;
    stack[stack_ptr] = l;
    stack[stack_ptr + 1] = r;
    stack_ptr += 2;
    while (stack_ptr > 0) {                 // while stack not empty
        r = stack[stack_ptr - 1];
        l = stack[stack_ptr - 2];
        stack_ptr -= 2;
        int p = partition(arr, l, r);
        if (p - 1 > l) {
            stack[stack_ptr] = l;
            stack[stack_ptr + 1] = p - 1;
            stack_ptr += 2;
        }
        if (p + 1 < r) {
            stack[stack_ptr] = p + 1;
            stack[stack_ptr + 1] = r;
            stack_ptr += 2;
        }
    }
}
```