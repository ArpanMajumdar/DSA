package com.arpan.leetcode.firstbadversion;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class FirstBadVersionSolutionTest {

    @Test
    void testFirstBadVersion() {
        // Arrange
        int n = 2126753390;
        int firstBadVersionNum = 1702766719;
        FirstBadVersionSolution firstBadVersionSolution = new FirstBadVersionSolution(firstBadVersionNum);

        int expectedResult = firstBadVersionNum;

        // Act
        int actualResult = firstBadVersionSolution.firstBadVersion(n);

        // Assert
        Assertions.assertEquals(expectedResult, actualResult);
    }

}