package com.arpan.dsa.sorting;

import java.util.Random;

public class RandomSequenceGenerator {

    public static int[] generateRandomSequence(int size,int min,int max){
        Random random=new Random();
        int[] arr=new int[size];

        for(int i=0;i<size;i++){
            arr[i]=random.nextInt((max-min)+1)+min;
        }
        return arr;
    }
}
