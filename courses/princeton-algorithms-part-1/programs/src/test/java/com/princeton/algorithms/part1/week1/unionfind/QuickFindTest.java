package com.princeton.algorithms.part1.week1.unionfind;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

class QuickFindTest {

    @Test
    void union() {
        // Arrange
        UnionFind quickFind = new QuickFind(10);

        // Act
        quickFind.union(4, 3);
        quickFind.union(3, 8);
        quickFind.union(6, 5);
        quickFind.union(9, 4);
        quickFind.union(1, 2);
        quickFind.union(5, 6);
        quickFind.union(1, 6);

        // Assert
        assertTrue(quickFind.find(8, 9));
        assertTrue(quickFind.find(1, 6));
        assertFalse(quickFind.find(0, 9));
    }

}