package com.arpan.dsa.algorithms.sorting;


import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;

public class InsertionSortDemoTest {

    @Test
    public void testInsertionSort() {
        // Setup
        InsertionSortDemo insertionSortDemo = new InsertionSortDemo();
        int[] arr = {5, 6, 3, 1, 2, 7, 4};
        int[] expectedArr = {1, 2, 3, 4, 5, 6, 7};

        // When
        insertionSortDemo.insertionSort(arr);

        // Then
        assertArrayEquals(expectedArr, arr);
    }
}