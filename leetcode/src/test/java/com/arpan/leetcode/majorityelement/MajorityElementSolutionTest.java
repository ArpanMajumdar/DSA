package com.arpan.leetcode.majorityelement;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class MajorityElementSolutionTest {

    @Test
    void majorityElement() {
        // Arrange
        MajorityElementSolution majorityElementSolution = new MajorityElementSolution();
        int[] nums = {2,2,1,1,1,2,2};
        int expectedResult = 2;

        // Act
        int actualResult = majorityElementSolution.majorityElement(nums);

        // Assert
        Assertions.assertEquals(expectedResult, actualResult);
    }
}