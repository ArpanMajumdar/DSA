package com.arpan.leetcode.happynumber;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class HappyNumberSolutionTest {

    @Test
    void isHappy() {
        // Arrange
        int n = 19;

        // Act
        HappyNumberSolution solution = new HappyNumberSolution();
        boolean actualResult = solution.isHappy(n);

        // Assert
        Assertions.assertTrue(actualResult);
    }
}