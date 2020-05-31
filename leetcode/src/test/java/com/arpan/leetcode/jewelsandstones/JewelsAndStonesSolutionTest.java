package com.arpan.leetcode.jewelsandstones;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class JewelsAndStonesSolutionTest {

    @Test
    void testNumJewelsInStones() {
        // Arrange
        JewelsAndStonesSolution jewelsAndStonesSolution = new JewelsAndStonesSolution();
        String J = "aA";
        String S = "aAAbbbb";
        Integer expectedResult = 3;

        // Act
        Integer actualResult = jewelsAndStonesSolution.numJewelsInStones(J, S);

        // Assert
        Assertions.assertEquals(expectedResult, actualResult);
    }
}