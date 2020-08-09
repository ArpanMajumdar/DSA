package com.arpan.leetcode.validpalindrome;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class ValidPalindromeSolutionTest {

    @Test
    void isPalindrome() {
        // Arrange
        String str1 = "A man, a plan, a canal: Panama";
        String str2 = "race a car";
        String str3 = "ab_a";


        // Act
        ValidPalindromeSolution solution = new ValidPalindromeSolution();
        boolean actualResult1 = solution.isPalindrome(str1);
        boolean actualResult2 = solution.isPalindrome(str2);
        boolean actualResult3 = solution.isPalindrome(str3);

        // Assert
        Assertions.assertTrue(actualResult1);
        Assertions.assertFalse(actualResult2);
        Assertions.assertTrue(actualResult3);
    }
}