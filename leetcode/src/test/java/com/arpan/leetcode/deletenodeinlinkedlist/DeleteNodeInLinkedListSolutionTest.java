package com.arpan.leetcode.deletenodeinlinkedlist;

import com.arpan.leetcode.common.ListNode;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class DeleteNodeInLinkedListSolutionTest {

    @Test
    void testDeleteNode() {
        // Arrange
        ListNode head = new ListNode(4);
        head.next = new ListNode(5);
        head.next.next = new ListNode(1);
        head.next.next.next = new ListNode(9);

        DeleteNodeInLinkedListSolution deleteNodeInLinkedListSolution = new DeleteNodeInLinkedListSolution();

        // Act
        deleteNodeInLinkedListSolution.deleteNode(head.next);

        // Assert
        assertEquals(4, head.val);
        assertEquals(1, head.next.val);
        assertEquals(9, head.next.next.val);
        assertNull(head.next.next.next);
    }
}