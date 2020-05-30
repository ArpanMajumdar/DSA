package com.arpan.leetcode.firstbadversion;

public class FirstBadVersionSolution {
    int firstBadVersionNum;

    public FirstBadVersionSolution(int firstBadVersionNum) {
        this.firstBadVersionNum = firstBadVersionNum;
    }

    public int firstBadVersion(int n) {
        return binarySearch(1, n);
    }

    public int binarySearch(int beg, int end) {
        while (beg < end) {
            int mid = beg + (end - beg) / 2;
            if (isBadVersion(mid)) {
                end = mid;
            } else {
                beg = mid + 1;
            }
        }
        return beg;
    }

    public boolean isBadVersion(int i) {
        return i >= firstBadVersionNum;
    }
}
