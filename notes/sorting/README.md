# Sorting

### Applications

- Maintain a phonebook
- Spreadsheets
- Problems become easy when items are sorted (finding a median)
- Binary search
- Compression (Sort the words according to their frequency)
- Computer graphics

## Insertion sort

- It is an efficient algorithm for sorting a small number of elements.
- The algorithm sorts the input numbers **in-place** i.e. it rearrranges the numbers wihin the array with at most a constant number of them stored outside the array at any time.

### Pseudocode

```
for j = 2 to A.length
    key = A[j]
    // Insert A[j] into sorted sequence A[1..j-1]
    
    for i = j - 1; i > 0 and A[i] > key; i-- 
        A[i + 1] = A[i]
      
    A[j + 1] = key
```
The index `j` indicates the current element being inserted to its position. The subarray consisting of elements `A[1..j-1]` is sorted and `A[j+1..n]` is unsorted.

### Implementations

1. [Java](../../algorithms/src/main/java/com/arpan/dsa/algorithms/sorting/InsertionSortDemo.java)


## Merge sort

The merge sort algorithm closely follows the **divide-and-conquer paradigm**. It operates as follows -

1. **Divide** - Divide the n-element sequence to be sorted into 2 subsequnces of `n/2` elements each.
2. **Conquer** - Sort the two subsequences recursively using merge sort.
3. **Combine** - Merge the two sorted subsequnces to produce sorted answer.

- The recursion bottoms out when sequence to be sorted has length 1, in which case there is no work to be done as it is already sorted.
- Key operation of merge sort is the merging of two sorted sequences in the combine step.

### Pseudocode

```
fun merge(A, p, q, r)
    leftSize = q - p + 1
    rightSize = r - q

    Let left[1..leftSize + 1] and right[1..rightSize + 1] be new arrays

    for i = 1 to leftSize
        left[i] = A[p + i - 1]

    for j = 1 to rightSize
        right[i] = A[q + j]

    left[leftSize + 1] = inf
    right[rightSize + 1] = inf

    for i = 1, j = 1, k = p; k <= r ; k++
        if left[i] < right[j]
            A[k] = left[i]
            i++
        else
            A[k] = right[j]
            j++

fun mergeSort(A, beg, end)
    if beg < end
        mid = (beg + end)/2

        mergeSort(A, beg, mid)
        mergeSort(A, mid + 1, end)
        merge(A, beg, mid, end)
```

## Heap sort

