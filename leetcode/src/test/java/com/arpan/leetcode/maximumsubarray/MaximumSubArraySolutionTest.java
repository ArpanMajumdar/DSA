package com.arpan.leetcode.maximumsubarray;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class MaximumSubArraySolutionTest {

    @Test
    void maxSubArray() {
        // Arrange
        int[] nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        int expectedResult = 6;

        // Act
        MaximumSubArraySolution solution = new MaximumSubArraySolution();
        int actualResult = solution.maxSubArray(nums);

        // Assert
        Assertions.assertEquals(expectedResult, actualResult);
    }

    @Test
    void testMaxSubArrayAllNegatives() {
        // Arrange
        int[] nums = {-2, -1, -5,-7};
        int expectedResult = -1;

        // Act
        MaximumSubArraySolution solution = new MaximumSubArraySolution();
        int actualResult = solution.maxSubArray(nums);

        // Assert
        Assertions.assertEquals(expectedResult, actualResult);
    }
}