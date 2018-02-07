package datastructures.stack;

import datastructures.queue.Queue;
import exceptions.QueueUnderflowException;

public class QueueUsingStack implements Queue {

    private Stack stack1;

    private Stack stack2;

    public QueueUsingStack() {
        stack1 = new StackLinkedListImpl();
        stack2 = new StackLinkedListImpl();
    }

    @Override
    public void enqueue(int x) {
        stack1.push(x);
    }

    @Override
    public int dequeue() {
        if (stack1.isEmpty() && stack2.isEmpty()) {
            throw new QueueUnderflowException("Queue underflow: No elements to dequeue");
        }
        if (stack2.isEmpty()) {
            while (!stack1.isEmpty()) {
                stack2.push(stack1.pop());
            }
        }
        return stack2.pop();
    }
}
