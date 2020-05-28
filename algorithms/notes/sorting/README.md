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

### Implementations

1. [Java](../../algorithms/src/main/java/com/arpan/dsa/algorithms/sorting/MergeSortDemo.java)

## Heap sort

### Heap

- Heap data structure is an array object that we can view as a complete binary tree.
- Each node of the tree corresponds to element of the array. Tree is complely filled at all levels except possibly the lowest, which is filled from left upto a point.
- An array A that represents a heap is an object with 2 attributes - `A.length` which gives the number of elements in the array and `A.heapSize` which represents how many elements in the heap are stored in array A.
- Although `A[1..A.length]` may contain numbers, only elements in `A[1..A.heapSize]` where `0 <= A.heapSize <= A.length` are valid elements of the heap.
- Root of the tree is `A[1]` and given the index i of a node, we can easily calculate indices of its parent, left child and right child.
- There are 2 kinds of binary heaps: **max heap** and **min heap**.
- In both kinds of heap, the values in node satisfy a **heap property**.
- In a **max heap**, for every node i other than root `A[parent(i)] >= A[i]`. Thus the largest element in the array is always stored as root.
- A **min heap** is organized in the opposite way i.e. for every node i other than root `A[parent(i)] <= A[i]`.
- **Height** of a node in a heap is the nuber of edges on the longest simple downward path from the node to the leaf and height of the heap is equal to height of the root.
- Since heap of n-elements is a complete binary tree, its height is `log(n)`.
- Heap is also used to implement priority queue data structure.
- In order to maintain max-heap property, we call `maxHeapify` function.

```
fun parent(i)
    return i/2

fun left(i)
    return 2*i

fun right(i)
    return 2*i + 1

fun maxHeapify(A, i)

    l = left(i)
    r = right(i)

    if l <= A.heapSize and A[l] > A[i]
        largest = l
    if r <= A.heapSize and A[r] > A[largest]
        largest = r

    if largest != i
        swap A[i] with A[largest]
        maxHeapify(A, largest)
```
- At each step, largest of elements `A[i]`, `A[left(i)]` and `A[right(i)]` is determined and its index is stored in the largest. If `A[i]` is largest, then subtree rooted at node i is already a max-heap and the function terminates.
- If one of the children has largest element, `A[i]` is swapped with `A[largest]` which cause node i to satisfy heap property. The node indexed by largest now has original value `A[i]` and thus may violate the max-heap property. Consequentl, we call `maxHeapify` on that subtree.
- Running time of `maxHeapify` on a subtree of size n is `O(h)` or `O(log n)`.

### Building a heap

- We can use `maxHeapify` function bottom-up to convert an array `A[1..n]` into a max heap.
- The elemnets of the array A[(n/2) + 1..n] are all one element heap to begin with.
- Function `buildMaxHeap()` goes through the remaining nodes of the tree and runs max-heapify for each one.

```
fun buildMaxHeap(A)
    A.heapSize = A.length
    for i = A.length / 2 down to 1
        maxHeapify(A, i)
```

### Heapsort algorithm

- Heapsort algorithm start by using `buildMaxHeap()` on th einput array `A[1..n]`.
- Since max element is stored at the root `A[1]` we can put it in its final correct position by exchanging it with A[n].
- We now discard node n from heap by decrementing the `A.heapSize`.
- The new root may violate the heap property. To restore the max-heap property, call `maxHeapify()` which creates a max heap in `A[1..n-1]`.
- Repeat this process for the max-heap of size `n-1` down to heap size of `2`.

```
fun heapSort(A)
    buildMaxHeap(A)
    
    for i = A.length down to 2
        exchange A[1] with A[i]
        A.heapSize = A.heapSIze - 1
        maxHeapify(A, 1)
```
