package com.arpan.dsa.datastructures.linkedlist;

public interface List {

  void insertAtBegin(int data);

  void insertAtEnd(int data);

  void insert(int data, int position);

  int removeFromBegin();

  int removeFromEnd();

  int remove(int data);

  int getLength();

  void printList();
}
