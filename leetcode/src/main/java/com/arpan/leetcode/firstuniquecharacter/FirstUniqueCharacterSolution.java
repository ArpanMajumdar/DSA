package com.arpan.leetcode.firstuniquecharacter;

public class FirstUniqueCharacterSolution {
    public int firstUniqChar(String s) {
        int[] charFreqArr = new int[26];
        int[] firstOccurrenceArr = new int[26];

        int index;
        for (int i = 0; i < s.length(); i++) {
            index = s.charAt(i) - 'a';
            charFreqArr[index]++;
            if (charFreqArr[index] == 1) {
                firstOccurrenceArr[index] = i;
            }
        }

        for (int i = 0; i < s.length(); i++) {
            index = s.charAt(i) - 'a';
            if (charFreqArr[index] == 1) {
                return firstOccurrenceArr[index];
            }
        }
        return -1;
    }
}
