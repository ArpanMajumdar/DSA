package com.arpan.leetcode.poweroffour;

public class PowerOfFourSolution {
    public boolean isPowerOfFour(int num) {
        if(num == 0) return false;
        double power = Math.log(num)/Math.log(4);
        return Math.floor(power) == power;
    }
}
