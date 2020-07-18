package com.arpan.leetcode.binarytreelevelordertraversal2;

import com.arpan.leetcode.common.TreeNode;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

class BinaryTreeLevelOrderTraversal2Test {

    @Test
    void levelOrderBottom() {
        // Arrange
        TreeNode root = new TreeNode(
            3,
            new TreeNode(9),
            new TreeNode(20, new TreeNode(15), new TreeNode(7))
        );

        List<List<Integer>> expected = Arrays.asList(
            Arrays.asList(15, 7),
            Arrays.asList(9, 20),
            Arrays.asList(3)
        );

        // Act
        BinaryTreeLevelOrderTraversal2 binaryTreeLevelOrderTraversal2 = new BinaryTreeLevelOrderTraversal2();
        List<List<Integer>> actual = binaryTreeLevelOrderTraversal2.levelOrderBottom(root);

        // Assert
        Assertions.assertTrue(assertNestedListEquals(expected, actual));
    }

    private boolean assertNestedListEquals(List<List<Integer>> expected, List<List<Integer>> actual) {
        if (expected.size() != actual.size()) return false;

        List<Integer> expectedInnerList;
        List<Integer> actualInnerList;
        for (int i = 0; i < expected.size(); i++) {
            expectedInnerList = expected.get(i);
            actualInnerList = actual.get(i);
            if (expectedInnerList.size() != actualInnerList.size()) return false;

            for (int j = 0; j < expectedInnerList.size(); j++) {
                if (!expectedInnerList.get(j).equals(actualInnerList.get(j))) return false;
            }
        }
        return true;
    }
}