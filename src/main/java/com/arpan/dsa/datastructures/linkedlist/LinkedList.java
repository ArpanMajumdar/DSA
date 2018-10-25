package com.arpan.dsa.datastructures.linkedlist;

public class LinkedList {

    private LinkedListNode head;

    private LinkedListNode tail;

    public LinkedListNode search(int key) {
        LinkedListNode curLinkedListNode = head;

        while (curLinkedListNode != null) {
            if (curLinkedListNode.data == key) {
                return curLinkedListNode;
            }
            curLinkedListNode = curLinkedListNode.next;
        }
        return null;
    }

    public void insert(int data) {
        LinkedListNode linkedListNode = new LinkedListNode(data);
        if (head == null) {
            head = linkedListNode;
            tail = linkedListNode;
        } else {
            tail.next = linkedListNode;
            linkedListNode.prev = tail;
            tail = linkedListNode;
        }
    }

    public void delete(LinkedListNode linkedListNode) {
        if (linkedListNode != null) {
            if (linkedListNode.prev != null) {
                linkedListNode.prev.next = linkedListNode.next;
            } else {
                head = linkedListNode.next;
            }
            if (linkedListNode.next != null) {
                linkedListNode.next.prev = linkedListNode.prev;
            } else {
                tail = linkedListNode.prev;
            }
        }
    }

    @Override
    public String toString() {
        LinkedListNode node = head;
        StringBuilder str = new StringBuilder();
        str.append("LinkedList: [");
        while (node != null) {
            str.append(node.data).append(" ->");
            node = node.next;
        }
        str.append(" ]");
        return str.toString();
    }
}
