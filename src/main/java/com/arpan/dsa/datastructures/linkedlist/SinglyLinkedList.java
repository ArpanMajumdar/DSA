package com.arpan.dsa.datastructures.linkedlist;

public class SinglyLinkedList implements List {

  private int length;

  private ListNode head;

  public SinglyLinkedList() {
    length = 0;
    head = null;
  }

  @Override
  public void insertAtBegin(int data) {
    ListNode listNode = new ListNode(data);

    // Head can be null in case of empty list
    listNode.setNext(head);
    head = listNode;
    length++;
  }

  @Override
  public void insertAtEnd(int data) {
    ListNode listNode = new ListNode(data);

    if (head == null) {
      head = listNode;
    } else {
      ListNode curNode = head;

      // Iterate till end of the list and add new node
      while (curNode.getNext() != null) {
        curNode = curNode.getNext();
      }
      curNode.setNext(listNode);
    }
    length++;
  }

  @Override
  public void insert(int data, int position) {
    // Assuming position is 0 based
    if (position == 0) {
      insertAtBegin(data);
    } else if (position == length) {
      insertAtEnd(data);
    } else if (position > 0 && position < length) {
      ListNode listNode = new ListNode(data);
      ListNode curNode = head;
      // Traverse to node one position before the given position
      for (int i = 0; i < position - 1; i++) {
        curNode = curNode.getNext();
      }
      // Step 1: Set next node of the new node to next node of cur node
      listNode.setNext(curNode.getNext());

      // Step 2: Set next node of cur node to new node
      curNode.setNext(listNode);
    } else {
      throw new RuntimeException(String.format("Position must be between %d and %d", 0, length));
    }
  }

  @Override
  public int removeFromBegin() {
    if (head != null) {
      int temp = head.getData();

      // Move the head pointer to next node
      head = head.getNext();
      return temp;
    } else {
      return 0;
    }
  }

  @Override
  public int removeFromEnd() {
    return 0;
  }

  @Override
  public int remove(int data) {
    return 0;
  }

  @Override
  public int getLength() {
    return this.length;
  }

  @Override
  public void printList() {}

  public ListNode getHead() {
    return head;
  }
}
