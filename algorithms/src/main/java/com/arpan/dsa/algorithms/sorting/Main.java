package com.arpan.dsa.algorithms.sorting;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        int[] arrBeforeSort = RandomSequenceGenerator.generateRandomSequence(10, 0, 100);

//        int[] arrBeforeSort = {79, 69, 32, 64, 64, 93, 18, 4, 51, 81};
        int[] arrAfterSort = Arrays.copyOf(arrBeforeSort, arrBeforeSort.length);

//        System.out.println("Before com.arpan.dsa.algorithms.sorting:");
//        Arrays.stream(arrBeforeSort).forEach(System.out::println);

        //Insertion sort
//        InsertionSortDemo.insertionSort(arrAfterSort);

        //Bubble sort
//        BubbleSortDemo.bubbleSort(arrAfterSort);

        //Merge sort
//        MergeSortDemo.mergeSortUtil(arrAfterSort);

        //Heap sort
//        HeapSortDemo.heapSort(arrAfterSort);

        //Quick sort demo
        QuickSortDemo.quickSortUtil(arrAfterSort);


//        System.out.println("After com.arpan.dsa.algorithms.sorting:");
//        Arrays.stream(arrAfterSort).forEach(System.out::println);

        Arrays.sort(arrBeforeSort);
        if (Arrays.equals(arrBeforeSort, arrAfterSort)) {
            System.out.println("Sorting successful... YO BITCH!!");
        } else {
            System.out.println("FUUUUUUUK... :(");
        }
    }
}
