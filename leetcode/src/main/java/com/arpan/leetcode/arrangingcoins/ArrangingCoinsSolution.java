package com.arpan.leetcode.arrangingcoins;

public class ArrangingCoinsSolution {
    public int arrangeCoins(int n) {
        long sum = (int) Math.sqrt(2 * (double) n);

        if ((sum * (sum + 1)) / 2 > n) return (int) (sum - 1);
        else return (int) sum;
    }
}
