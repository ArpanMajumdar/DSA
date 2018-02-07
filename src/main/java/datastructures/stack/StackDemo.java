package datastructures.stack;

public class StackDemo {

    public static void main(String[] args) {
        //Array implementation
        Stack stackArray = new StackArrayImpl();
        stackArray.push(1);
        stackArray.push(2);
        stackArray.push(3);
        stackArray.push(4);

        System.out.println("Array implementation:");
        for (int i = 0; i < 4; i++) {
            System.out.println(stackArray.pop());
        }

        System.out.println();

        //Linked list implementation
        Stack stackLinkedList = new StackLinkedListImpl();
        stackLinkedList.push(1);
        stackLinkedList.push(2);
        stackLinkedList.push(3);
        stackLinkedList.push(4);
        System.out.println("Linked list implementation:");
        for (int i = 0; i < 5; i++) {
            System.out.println(stackLinkedList.pop());
        }
    }
}
