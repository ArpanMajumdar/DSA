package com.arpan.dsa.datastructures.stack;

import com.arpan.dsa.datastructures.queue.Queue;

public class QueueUsingStackDemo {

    public static void main(String[] args) {
        Queue queue=new QueueUsingStack();

        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);
        queue.enqueue(4);
        queue.enqueue(5);

        for (int i=0;i<6;i++){
            System.out.println(queue.dequeue());
        }
    }
}
