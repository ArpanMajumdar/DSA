package datastructures.stack;

import exceptions.StackUnderflowException;

import java.util.LinkedList;
import java.util.List;

public class StackLinkedListImpl implements Stack {

    private List<Integer> list;

    public StackLinkedListImpl() {
        this.list = new LinkedList<>();
    }

    @Override
    public boolean isEmpty() {
        return list.isEmpty();
    }

    @Override
    public void push(int x) {
        list.add(x);
    }

    @Override
    public int pop() {
        if (list.isEmpty()) {
            throw new StackUnderflowException("Stack Underflow. No elements to pop.");
        }

        int x = list.get(list.size() - 1);
        list.remove(list.size() - 1);
        return x;
    }

    @Override
    public int peek() {
        return list.get(list.size() - 1);
    }
}
