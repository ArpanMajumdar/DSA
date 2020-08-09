package com.arpan.leetcode.validpalindrome;

public class ValidPalindromeSolution {
    public boolean isPalindrome(String s) {
        // "A man, a plan, a canal: Panama"

        String normalizedStr = s.toLowerCase().replaceAll("[^a-zA-Z0-9]+", "");
        System.out.println(normalizedStr);
        int beg = 0;
        int end = normalizedStr.length() - 1;

        while (beg < end) {
            if (normalizedStr.charAt(beg) != normalizedStr.charAt(end)) return false;
            beg++;
            end--;
        }
        return true;
    }
}
