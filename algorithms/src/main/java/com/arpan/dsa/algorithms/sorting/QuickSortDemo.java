package com.arpan.dsa.algorithms.sorting;

import com.arpan.dsa.util.ArrayUtil;

public class QuickSortDemo {

    public int partition(int[] arr, int beg, int end) {
        int pivot = arr[end];
        int i = beg - 1;

        for (int j = beg; j < end; j++) {
            if (arr[j] < pivot) {
                i++;
                ArrayUtil.swap(arr, i, j);
            }
        }
        ArrayUtil.swap(arr, i + 1, end);
        return i + 1;
    }

    private void quickSortUtil(int[] arr, int beg, int end) {
        if (beg < end) {
            int pivotIndex = partition(arr, beg, end);
            quickSortUtil(arr, beg, pivotIndex - 1);
            quickSortUtil(arr, pivotIndex + 1, end);
        }
    }

    public void quickSort(int[] arr) {
        if (arr.length > 1) {
            quickSortUtil(arr, 0, arr.length - 1);
        }
    }
}
