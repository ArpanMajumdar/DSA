package com.arpan.leetcode.islandperimeter;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class IslandPerimeterSolutionTest {

    @Test
    void islandPerimeter() {
        // Arrange
        int[][] grid = {{0, 1, 0, 0}, {1, 1, 1, 0}, {0, 1, 0, 0}, {1, 1, 0, 0}};
        int actual = 16;

        // Act
        IslandPerimeterSolution islandPerimeterSolution = new IslandPerimeterSolution();
        int expected = islandPerimeterSolution.islandPerimeter(grid);

        // Assert
        Assertions.assertEquals(expected, actual);
    }
}