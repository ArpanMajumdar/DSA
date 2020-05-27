package com.arpan.dsa.algorithms.sorting;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;

class MergeSortDemoTest {
    @Test
    public void testMergeSort() {
        // Setup
        MergeSortDemo mergeSortDemo = new MergeSortDemo();
        int[] arr = {5, 6, 3, 1, 2, 7, 4};
        int[] expectedArr = {1, 2, 3, 4, 5, 6, 7};

        // When
        mergeSortDemo.mergeSort(arr);

        // Then
        assertArrayEquals(expectedArr, arr);
    }

    @Test
    public void testMerge() {
        // Setup
        int[] arr = {1, 3, 5, 8, 4, 6, 7, 9};
        int beg = 0, mid = 3, end = 7;
        MergeSortDemo mergeSortDemo = new MergeSortDemo();

        int[] expectedArr = {1, 3, 4, 5, 6, 7, 8, 9};

        // When
        mergeSortDemo.merge(arr, beg, mid, end);

        // Then
        assertArrayEquals(expectedArr, arr);
    }
}