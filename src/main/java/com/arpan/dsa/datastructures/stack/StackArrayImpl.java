package com.arpan.dsa.datastructures.stack;

import com.arpan.dsa.exceptions.StackOverflowException;
import com.arpan.dsa.exceptions.StackUnderflowException;

public class StackArrayImpl implements Stack {

    private static int MAX = 100;

    private int top;

    private int[] arr;

    StackArrayImpl() {
        arr = new int[MAX];
        top = -1;
    }

    @Override
    public boolean isEmpty() {
        return top == -1;
    }

    @Override
    public void push(int x) {
        if (top == MAX - 1) {
            throw new StackOverflowException("Stack Overflow. Cannot insert more elements.");
        }
        arr[++top] = x;
    }

    @Override
    public int pop() {
        if (top == -1) {
            throw new StackUnderflowException("Stack Underflow. No elements to pop.");
        }
        return arr[top--];
    }

    @Override
    public int peek() {
        return arr[top];
    }
}
