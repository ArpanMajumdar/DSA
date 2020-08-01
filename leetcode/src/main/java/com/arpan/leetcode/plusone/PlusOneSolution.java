package com.arpan.leetcode.plusone;

public class PlusOneSolution {
    public int[] plusOne(int[] digits) {
        int n = digits.length;

        int carry = 0;
        int sum = 0;
        for(int i = n-1; i>= 0; i--){
            sum = digits[i] + carry;
            if(i == n-1){
                sum++;
            }
            digits[i] = sum % 10;
            carry = sum / 10;
            if(carry == 0){
                break;
            }
        }

        // Handle case when carry overflows for most significant digit
        if(carry != 0){
            int[] digitsOverflow = new int[n+1];
            digitsOverflow[0] = carry;
            for(int i=1; i<n+1; i++){
                digitsOverflow[i] = digits[i-1];
            }
            return digitsOverflow;
        }
        return  digits;
    }
}
