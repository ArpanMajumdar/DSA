package com.arpan.leetcode.threesum;

import org.junit.jupiter.api.Test;

import java.util.List;

class ThreeSumSolutionTest {

    @Test
    void threeSum() {
        // Arrange
        int[] nums = {1, 2, -2, -1};

        // Act
        ThreeSumSolution threeSumSolution = new ThreeSumSolution();
        List<List<Integer>> actual = threeSumSolution.threeSum(nums);

        // Assert
        actual.forEach(numList -> {
                numList.forEach(num -> System.out.print(num + "\t"));
                System.out.println();
            }
        );
    }
}