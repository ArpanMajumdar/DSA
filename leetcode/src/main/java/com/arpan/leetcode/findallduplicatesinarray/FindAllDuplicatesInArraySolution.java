package com.arpan.leetcode.findallduplicatesinarray;

import java.util.ArrayList;
import java.util.List;

public class FindAllDuplicatesInArraySolution {
    public List<Integer> findDuplicates(int[] nums) {
        int[] freq = new int[nums.length];
        List<Integer> duplicates = new ArrayList<>();

        for (int num : nums) {
            freq[num - 1]++;
            if (freq[num - 1] == 2) {
                duplicates.add(num);
            }
        }

//        duplicates.forEach(el -> System.out.print(el + " "));
//        System.out.println();

        return duplicates;
    }

}
