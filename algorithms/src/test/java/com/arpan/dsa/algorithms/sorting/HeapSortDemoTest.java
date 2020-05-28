package com.arpan.dsa.algorithms.sorting;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;

class HeapSortDemoTest {

    @Test
    void testMaxHeapify() {
        // Arrange
        int[] arr = {16, 4, 10, 14, 7, 9, 3, 2, 8, 1};
        int[] expectedArr = {16, 14, 10, 8, 7, 9, 3, 2, 4, 1};
        HeapSortDemo heapSortDemo = new HeapSortDemo();

        // Act
        heapSortDemo.maxHeapify(arr, 1, arr.length);

        // Assert
        assertArrayEquals(expectedArr, arr);
    }

    @Test
    void testBuildMaxHeap() {
        // Arrange
        int[] arr = {4, 1, 3, 2, 16, 9, 10, 14, 8, 7};
        int[] expectedArr = {16, 14, 10, 8, 7, 9, 3, 2, 4, 1};
        HeapSortDemo heapSortDemo = new HeapSortDemo();

        // Act
        heapSortDemo.buildMaxHeap(arr);

        // Assert
        assertArrayEquals(expectedArr, arr);
    }

    @Test
    void testHeapSort() {
        // Arrange
        int[] arr = {16, 14, 10, 8, 7, 9, 3, 2, 4, 1};
        int[] expectedArr = {1, 2, 3, 4, 7, 8, 9, 10, 14, 16};
        HeapSortDemo heapSortDemo = new HeapSortDemo();

        // Act
        heapSortDemo.heapSort(arr);

        // Assert
        assertArrayEquals(expectedArr, arr);
    }
}