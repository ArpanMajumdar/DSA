package com.arpan.leetcode.invertbinarytree;

import com.arpan.leetcode.common.TreeNode;

public class InvertBinaryTreeSolution {
        public TreeNode invertTree(TreeNode root) {
            if(root == null) return null;
            if(root.left == null && root.right == null) return root;

            TreeNode temp;
            temp = invertTree(root.left);
            root.left = invertTree(root.right);
            root.right = temp;
            return root;
        }
}
