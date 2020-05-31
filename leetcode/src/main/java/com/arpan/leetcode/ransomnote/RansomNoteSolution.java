package com.arpan.leetcode.ransomnote;

public class RansomNoteSolution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] ransomNotesChars = new int[26];
        int[] magazineChars = new int[26];

        int index;
        for (int i = 0; i < magazine.length(); i++) {
            index = magazine.charAt(i) - 'a';
            magazineChars[index]++;
        }

        for (int i = 0; i < ransomNote.length(); i++) {
            index = ransomNote.charAt(i) - 'a';
            ransomNotesChars[index]++;
        }

        boolean flag = true;
        for (int i = 0; i < 26; i++) {
            if (ransomNotesChars[i] != 0 && ransomNotesChars[i] > magazineChars[i]) {
                flag = false;
                break;
            }
        }
        return flag;
    }
}
