package com.arpan.dsa.algorithms.sorting;

import com.arpan.dsa.util.ArrayUtil;

public class HeapSortDemo {

    private int getParent(int i) {
        return (i - 1) / 2;
    }

    private int getLeftChild(int i) {
        return 2 * i + 1;
    }

    private int getRightChild(int i) {
        return 2 * i + 2;
    }

    public void maxHeapify(int[] arr, int i, int heapSize) {
        int left = getLeftChild(i);
        int right = getRightChild(i);
        int largest = i;

        if (left < heapSize && arr[left] > arr[i]) {
            largest = left;
        }
        if (right < heapSize && arr[right] > arr[largest]) {
            largest = right;
        }
        if (largest < heapSize && largest != i) {
            ArrayUtil.swap(arr, largest, i);
            maxHeapify(arr, largest, heapSize);
        }
    }

    public void buildMaxHeap(int[] arr) {
        int heapSize = arr.length;

        for (int i = (heapSize - 1) / 2; i >= 0; i--) {
            maxHeapify(arr, i, heapSize);
        }
    }

    public void heapSort(int[] arr) {
        int heapSize = arr.length;
        buildMaxHeap(arr);
        for (int i = arr.length - 1; i > 0; i--) {
            ArrayUtil.swap(arr, 0, i);
            heapSize--;
            maxHeapify(arr, 0, heapSize);
        }
    }
}
