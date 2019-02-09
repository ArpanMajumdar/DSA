package com.arpan.dsa.algorithms.divideandconquer.inversions;

import com.arpan.dsa.algorithms.sorting.RandomSequenceGenerator;

import java.util.Arrays;

public class Main {
  public static void main(String[] args) {
    //
    int[] arr = RandomSequenceGenerator.generateRandomSequence(15, 1, 100);

    System.out.println("Given array:");
    System.out.println(Arrays.toString(arr));

    // Brute force implementation of number of inversions
    System.out.println("Inversions:");
    int sum = 0, count = 0;
    for (int i = 0; i < arr.length-1; i++) {
      for (int j = i + 1; j < arr.length; j++) {
        if (i < j && arr[i] > arr[j]) {
          System.out.println("[" + arr[i] + "," + arr[j] + "]");
          sum++;
        }
      }
    }

    int expectedInv = sum;

    int actualInv = InversionsDemo.countNumberOfInv(arr);

    System.out.println("Expected inversions: " + expectedInv);
    System.out.println("Actual inversions: " + actualInv);
    System.out.println(expectedInv == actualInv);
  }
}
