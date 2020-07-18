package com.arpan.leetcode.hammingdistance;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class HammingDistanceSolutionTest {

    @Test
    void hammingDistance() {
        // Arrange
        int x = 1;
        int y = 4;

        int expected = 2;
        // Act
        HammingDistanceSolution hammingDistanceSolution = new HammingDistanceSolution();
        int actual = hammingDistanceSolution.hammingDistance(x, y);

        // Assert
        Assertions.assertEquals(expected, actual);
    }
}