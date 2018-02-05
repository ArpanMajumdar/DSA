package sorting;

import util.ArrayUtil;

public class QuickSortDemo {

    private static int partition(int[] arr, int beg, int end) {
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

    private static void quickSort(int[] arr, int beg, int end) {
        if (beg < end) {
            int pivotIndex = partition(arr, beg, end);
            quickSort(arr, beg, pivotIndex - 1);
            quickSort(arr, pivotIndex + 1, end);
        }
    }

    public static void quickSortUtil(int[] arr) {
        if (arr.length > 1) {
            quickSort(arr, 0, arr.length - 1);
        }
    }
}
