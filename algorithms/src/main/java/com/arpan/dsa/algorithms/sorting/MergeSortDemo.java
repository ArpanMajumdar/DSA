package com.arpan.dsa.algorithms.sorting;

public class MergeSortDemo {

    public void mergeSort(int[] arr) {
        mergeSortUtil(arr, 0, arr.length - 1);
    }

    public void mergeSortUtil(int[] arr, int beg, int end) {
        if (beg < end) {
            int mid = (beg + end) / 2;

            mergeSortUtil(arr, beg, mid);
            mergeSortUtil(arr, mid + 1, end);
            merge(arr, beg, mid, end);
        }
    }

    public void merge(int[] arr, int beg, int mid, int end) {
        //l1[beg..mid]
        int l1 = mid - beg + 1;

        //l2[mid+1..end]
        int l2 = end - mid;

        int[] left = new int[l1 + 1];
        int[] right = new int[l2 + 1];

        //Copy elements b/w beg and mid to left array
        int index = 0;
        for (int i = beg; i <= mid; i++, index++) {
            left[index] = arr[i];
        }

        //Set last element to infinity
        left[index] = Integer.MAX_VALUE;

        //Copy elements b/w mid+1 and end to right array
        index = 0;
        for (int i = mid + 1; i <= end; i++, index++) {
            right[index] = arr[i];
        }

        //Set last element to infinity
        right[index] = Integer.MAX_VALUE;


        //Merge elements from left and right array into arr so that resulting array is sorted
        for (int i = 0, j = 0, k = beg; k <= end; k++) {
            if (left[i] < right[j]) {
                arr[k] = left[i];
                i++;
            } else {
                arr[k] = right[j];
                j++;
            }
        }
    }
}
