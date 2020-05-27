package com.arpan.dsa.algorithms.sorting;

public class InsertionSortDemo {

    public void insertionSort(int[] arr) {
        if (arr.length <= 1) return;

        int key;
        int j;
        for (int i = 1; i < arr.length; i++) {
            key = arr[i];

            for (j = i - 1; j >= 0 && arr[j] > key; j--) {
                arr[j + 1] = arr[j];
            }
            arr[j + 1] = key;
        }

    }
}
