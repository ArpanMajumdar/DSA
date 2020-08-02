package com.arpan.leetcode.maximumsubarray;

public class MaximumSubArraySolution {
    public int maxSubArray(int[] nums) {
        int globalSum = nums[0];
        int localSum = nums[0];
        for (int i = 1; i < nums.length; i++) {
            localSum = Math.max(nums[i], localSum + nums[i]);
            globalSum = Math.max(localSum, globalSum);
//            System.out.println("Local sum: " + localSum);
//            System.out.println("Global sum: " + globalSum);
        }
        return globalSum;
    }
}
