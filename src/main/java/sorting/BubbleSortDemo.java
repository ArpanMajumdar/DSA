package sorting;

import java.util.Arrays;

public class BubbleSortDemo {

    public static void bubbleSort(int[] arr) {

        int N = arr.length;
        boolean flag;

        for (int i = 0; i < N - 1; i++) {
            flag = false;
            for (int j = 1; j < N - i; j++) {
                if (arr[j] < arr[j - 1]) {
                    swap(arr, j, j - 1);
                    flag = true;
                }
            }
            if (!flag) {
                break;
            }
        }
    }

    private static void swap(int[] arr, int index1, int index2) {
        int temp = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = temp;
    }

}
