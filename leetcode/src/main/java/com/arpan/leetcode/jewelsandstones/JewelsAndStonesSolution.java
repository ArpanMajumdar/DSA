package com.arpan.leetcode.jewelsandstones;

import java.util.HashMap;
import java.util.Map;

public class JewelsAndStonesSolution {
    public int numJewelsInStones(String J, String S) {
        Map<Character, Integer> stoneCount = new HashMap<>();

        for (int i = 0; i < J.length(); i++) {
            stoneCount.put(J.charAt(i), 0);
        }

        for (int i = 0; i < S.length(); i++) {
            Character stone = S.charAt(i);
            stoneCount.computeIfPresent(stone, (k, v) -> v + 1);
        }

        return stoneCount.values().stream().reduce(0, Integer::sum);
    }
}

