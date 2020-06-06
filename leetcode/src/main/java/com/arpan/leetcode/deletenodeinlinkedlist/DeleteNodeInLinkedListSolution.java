package com.arpan.leetcode.deletenodeinlinkedlist;

import com.arpan.leetcode.common.ListNode;

public class DeleteNodeInLinkedListSolution {
    public void deleteNode(ListNode node) {
        ListNode cur = node;
        ListNode prev = node;
        while (cur.next!=null){
            cur.val = cur.next.val;
            prev = cur;
            cur = cur.next;
        }
        prev.next = null;
    }
}
