package com.arpan.leetcode.ransomnote;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class RansomNoteSolutionTest {

    @Test
    void testCanConstruct() {
        // Arrange
        RansomNoteSolution ransomNoteSolution = new RansomNoteSolution();
        String ransomNote = "a";
        String magazine = "b";

        // Act
        boolean actualResult = ransomNoteSolution.canConstruct(ransomNote, magazine);

        // Assert
        Assertions.assertFalse(actualResult);
    }
}