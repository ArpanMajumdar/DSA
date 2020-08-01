package com.arpan.leetcode.singlenumber;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class SingleNumberSolutionTest {

    @Test
    void singleNumber() {
        // Arrange
        int[] nums = {2, 2, 1, 3, 4, 5, 4, 5, 3};
        int expectedResult = 1;

        // Act
        SingleNumberSolution solution = new SingleNumberSolution();
        int actualResult = solution.singleNumber(nums);

        // Assert
        Assertions.assertEquals(expectedResult, actualResult);
    }
}