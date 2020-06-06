package com.arpan.leetcode.invertbinarytree;

import com.arpan.leetcode.common.TreeNode;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class InvertBinaryTreeSolutionTest {

    @Test
    public void testInvertTree(){
        // Arrange
        TreeNode root = new TreeNode(4,
                new TreeNode(2,
                        new TreeNode(1, null, null),
                        new TreeNode(3, null, null)),
                new TreeNode(7,
                        new TreeNode(6, null, null),
                        new TreeNode(9, null, null)));

        InvertBinaryTreeSolution invertBinaryTreeSolution = new InvertBinaryTreeSolution();

        // Act
        TreeNode actualResult = invertBinaryTreeSolution.invertTree(root);

        // Assert
        assertEquals(4, actualResult.val);
        assertEquals(7, actualResult.left.val);
        assertEquals(2, actualResult.right.val);
        assertEquals(9, actualResult.left.left.val);
        assertEquals(9, actualResult.left.left.val);
        assertEquals(6, actualResult.left.right.val);
        assertEquals(3, actualResult.right.left.val);
        assertEquals(1, actualResult.right.right.val);
    }
}