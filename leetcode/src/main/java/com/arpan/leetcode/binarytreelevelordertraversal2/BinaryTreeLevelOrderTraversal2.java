package com.arpan.leetcode.binarytreelevelordertraversal2;

import com.arpan.leetcode.common.TreeNode;

import java.util.*;

public class BinaryTreeLevelOrderTraversal2 {
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        if(root == null) return new LinkedList<>();
        Deque<TreeNodeWithLevel> deque = new LinkedList<>();
        Deque<TreeNodeWithLevel> deque2 = new LinkedList<>();
        deque.offer(new TreeNodeWithLevel(root, 1));

        TreeNodeWithLevel curNode;
        int numLevels = 1;
        while (!deque.isEmpty()) {
            curNode = deque.poll();
            if (curNode != null && curNode.node != null && curNode.node.left != null) {
                deque.offer(new TreeNodeWithLevel(curNode.node.left, curNode.level + 1));
                numLevels = Math.max(numLevels, curNode.level + 1);
            }
            if (curNode != null && curNode.node != null && curNode.node.right != null) {
                deque.offer(new TreeNodeWithLevel(curNode.node.right, curNode.level + 1));
                numLevels = Math.max(numLevels, curNode.level + 1);
            }
            deque2.offer(curNode);
        }

        List<List<Integer>> levels = new LinkedList<>();

        for (int i = 1; i <= numLevels; i++) {
            List<Integer> level = new ArrayList<>();
            curNode = deque2.poll();
            while (curNode != null && curNode.level == i) {
                level.add(curNode.node.val);
                curNode = deque2.poll();
            }
            deque2.addFirst(curNode);
            levels.add(level);
        }
        Collections.reverse(levels);
        return levels;
    }

    static class TreeNodeWithLevel {
        private final TreeNode node;
        private final int level;

        public TreeNodeWithLevel(TreeNode node, int level) {
            this.node = node;
            this.level = level;
        }
    }
}
