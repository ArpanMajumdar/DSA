package com.arpan.dsa.algorithms.sorting;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class QuickSortDemoTest {

    @Test
    void testPartition() {
        // Arrange
        QuickSortDemo quickSortDemo = new QuickSortDemo();
        int[] arr = {2, 8, 7, 1, 3, 5, 6, 4};
        int[] expectedArr = {2, 1, 3, 4, 7, 5, 6, 8};

        // Act
        quickSortDemo.partition(arr, 0, arr.length - 1);

        // Assert
        Assertions.assertArrayEquals(expectedArr, arr);
    }

    @Test
    void quickSort() {
        // Arrange
        QuickSortDemo quickSortDemo = new QuickSortDemo();
        int[] arr = {2, 8, 7, 1, 3, 5, 6, 4};
        int[] expectedArr = {1, 2, 3, 4, 5, 6, 7, 8};

        // Act
        quickSortDemo.quickSort(arr);

        // Assert
        Assertions.assertArrayEquals(expectedArr, arr);
    }
}