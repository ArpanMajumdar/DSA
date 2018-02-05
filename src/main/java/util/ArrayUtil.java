package util;

import java.util.Arrays;

public class ArrayUtil {

    public static void printArray(int[] arr) {
//        System.out.print("Array: [");
//        Arrays.stream(arr).forEach(e -> System.out.print(e + "\t"));
//        System.out.print("]\n");

        System.out.println(Arrays.toString(arr));
    }

    public static void swap(int[] arr, int index1, int index2) {
        int temp = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = temp;
    }
}
