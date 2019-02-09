package com.arpan.dsa.algorithms.divideandconquer.inversions;

public class InversionsDemo {

  public static int countNumberOfInv(int[] arr) {
    System.out.println("Subarrays:");
    return sortAndCount(arr, 0, arr.length - 1);
  }

  public static int sortAndCount(int[] arr, int beg, int end) {
    if (beg < end) {
      int mid = (beg + end) / 2;

      // Count left inversions
      int numLeftInv = sortAndCount(arr, beg, mid);

      // Count right inversions
      int numRightInv = sortAndCount(arr, mid + 1, end);

      // Count split inversions
      int numSplitInv = mergeAndCountSplitInversions(arr, beg, mid, end);

      return numLeftInv + numRightInv + numSplitInv;
    }
    return 0;
  }

  public static int mergeAndCountSplitInversions(int[] arr, int beg, int mid, int end) {
    // l1[beg..mid]
    int l1 = mid - beg + 1;

    // l2[mid+1..end]
    int l2 = end - mid;

    int[] left = new int[l1 + 1];
    int[] right = new int[l2 + 1];

    // Copy elements b/w beg and mid to left array
    int index = 0;
    for (int i = beg; i <= mid; i++, index++) {
      left[index] = arr[i];
    }

    // Set last element to infinity
    left[index] = Integer.MAX_VALUE;

    // Copy elements b/w mid+1 and end to right array
    index = 0;
    for (int i = mid + 1; i <= end; i++, index++) {
      right[index] = arr[i];
    }

    // Set last element to infinity
    right[index] = Integer.MAX_VALUE;

    int sum = 0;
    // Merge elements from left and right array into arr so that resulting array is sorted
    for (int i = 0, j = 0, k = beg; k <= end; k++) {
      if (left[i] < right[j]) {
        arr[k] = left[i];
        i++;
        if (i > l1) i = l1;
      } else {
        if (left[i] > right[j]) {
          sum += l1 - i;
        }
        arr[k] = right[j];
        j++;
      }
    }
    /*System.out.println(Arrays.toString(Arrays.copyOfRange(left, 0, left.length - 1)));
    System.out.println(Arrays.toString(Arrays.copyOfRange(right, 0, right.length - 1)));
    System.out.println(Arrays.toString(Arrays.copyOfRange(arr, beg, end + 1)));
    System.out.println("Sum: " + sum);
    System.out.println();*/
    return sum;
  }
}
