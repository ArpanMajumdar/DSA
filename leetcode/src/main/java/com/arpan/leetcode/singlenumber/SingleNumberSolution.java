package com.arpan.leetcode.singlenumber;

import java.util.HashMap;
import java.util.Map;

public class SingleNumberSolution {
    public int singleNumber(int[] nums) {

        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : nums) {
            freq.putIfAbsent(num, 0);
            freq.computeIfPresent(num, (k, v) -> v + 1);
        }

        for(Map.Entry<Integer, Integer> entry : freq.entrySet()){
            if(entry.getValue() == 1) return entry.getKey();
        }
        return 0;
    }
}
