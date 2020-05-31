package com.arpan.leetcode.majorityelement;

import java.util.HashMap;
import java.util.Map;

public class MajorityElementSolution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> freqMap = new HashMap<>();

        int n = nums.length;
        Integer freq;
        for (int num : nums) {
            freq = freqMap.get(num);

            if (freq != null) {
                freqMap.put(num, freq + 1);
            } else {
                freqMap.put(num, 1);
            }

            if (freqMap.get(num) > n / 2) {
                return num;
            }
        }
        return 0;
    }
}
