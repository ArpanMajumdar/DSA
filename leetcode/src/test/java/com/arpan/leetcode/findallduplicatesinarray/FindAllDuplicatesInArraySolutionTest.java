package com.arpan.leetcode.findallduplicatesinarray;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

class FindAllDuplicatesInArraySolutionTest {

    @Test
    void findDuplicates() {
        // Arrange
        int[] nums = {4, 3, 2, 7, 8, 2, 3, 1};
        List<Integer> expectedResult = Arrays.asList(2, 3);

        // Act
        FindAllDuplicatesInArraySolution solution = new FindAllDuplicatesInArraySolution();
        List<Integer> actualResult = solution.findDuplicates(nums);

        // Assert
        Assertions.assertEquals(expectedResult.size(), actualResult.size());
        for (int i = 0; i < expectedResult.size(); i++) {
            Assertions.assertEquals(expectedResult.get(i), actualResult.get(i));
        }
    }
}