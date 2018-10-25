package com.arpan.dsa.sorting;

import com.arpan.dsa.util.ArrayUtil;

public class BubbleSortDemo {

    public static void bubbleSort(int[] arr) {

        int N = arr.length;
        boolean flag;

        for (int i = 0; i < N - 1; i++) {
            flag = false;
            for (int j = 1; j < N - i; j++) {
                if (arr[j] < arr[j - 1]) {
                    ArrayUtil.swap(arr, j, j - 1);
                    flag = true;
                }
            }
            if (!flag) {
                break;
            }
        }
    }



}
