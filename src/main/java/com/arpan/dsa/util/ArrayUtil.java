package com.arpan.dsa.util;

import java.util.Arrays;

public class ArrayUtil {

  public static void printArray(int[] arr) {
    System.out.println(Arrays.toString(arr));
  }

  public static void swap(int[] arr, int index1, int index2) {
    int temp = arr[index1];
    arr[index1] = arr[index2];
    arr[index2] = temp;
  }
}
