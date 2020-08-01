package com.arpan.leetcode.plusone;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class PlusOneSolutionTest {

    @Test
    void plusOne() {
        // Arrange
        int[] digits = {9, 9, 9, 9, 9, 9, 9, 9};
        int[] expected = {1, 0, 0, 0, 0, 0, 0, 0, 0};

        // Act
        PlusOneSolution plusOneSolution = new PlusOneSolution();
        int[] actual = plusOneSolution.plusOne(digits);

        // Assert
        Assertions.assertArrayEquals(expected, actual);
    }
}