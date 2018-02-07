package datastructures.linkedlist;

public class LinkedListDemo {
    public static void main(String[] args) {
        LinkedList linkedList=new LinkedList();
        linkedList.insert(1);
        linkedList.insert(2);
        linkedList.insert(3);
        linkedList.insert(4);
        linkedList.insert(5);

        System.out.println(linkedList);

        LinkedListNode node=linkedList.search(4);
        linkedList.delete(node);

        node=linkedList.search(5);
        linkedList.delete(node);

        System.out.println(linkedList);

    }
}
