package sorting;

import java.util.Arrays;

public class InsertionSortDemo {

    public static void insertionSort(int[] arr){

        if(arr.length>1){
            int key,j;
            for(int i=1;i<arr.length;i++){
                key=arr[i];
                j=i-1;

                while (j>=0 && arr[j]>key){
                    arr[j+1]=arr[j];
                    j--;
                }
                arr[j+1]=key;
            }
        }
    }
}
