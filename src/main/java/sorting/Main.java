package sorting;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        int[] arrBeforeSort = RandomSequenceGenerator.generateRandomSequence(100, 0, 100);

        int[] arrAfterSort = Arrays.copyOf(arrBeforeSort, arrBeforeSort.length);

//        System.out.println("Before sorting:");
//        Arrays.stream(arrBeforeSort).forEach(System.out::println);

        //Insertion sort
//        InsertionSortDemo.insertionSort(arrAfterSort);

        //Bubble sort
//        BubbleSortDemo.bubbleSort(arrAfterSort);

        //Merge sort
        MergeSortDemo.mergeSortUtil(arrAfterSort);




//        System.out.println("After sorting:");
//        Arrays.stream(arrAfterSort).forEach(System.out::println);

        Arrays.sort(arrBeforeSort);
        if (Arrays.equals(arrBeforeSort, arrAfterSort)) {
            System.out.println("Sorting successfull... YO BITCH!!");
        } else {
            System.out.println("FUUUUUUUK... :(");
        }
    }
}
