package com.arpan.leetcode.happynumber;

import java.util.HashSet;
import java.util.Set;

public class HappyNumberSolution {
    public boolean isHappy(int n) {
        int squareSum;
        Set<Integer> prevSquareSums = new HashSet<>();
        while (n != 1) {
            squareSum = calcSquareSum(n);
            if (prevSquareSums.contains(squareSum)) {
                return false;
            } else {
                prevSquareSums.add(squareSum);
            }
            n = squareSum;
        }
        return true;
    }

    private int calcSquareSum(int n) {
        int sum = 0;
        int lastDigit;
        while (n > 0) {
            lastDigit = n % 10;
            sum += (lastDigit * lastDigit);
            n = n / 10;
        }
        return sum;
    }
}
