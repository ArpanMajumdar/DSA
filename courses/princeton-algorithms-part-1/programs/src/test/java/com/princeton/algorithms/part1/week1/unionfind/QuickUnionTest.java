package com.princeton.algorithms.part1.week1.unionfind;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class QuickUnionTest {

    @Test
    void testQuickUnion() {
        // Arrange
        UnionFind quickUnion = new QuickUnion(10);

        // Act
        quickUnion.union(4, 3);
        quickUnion.union(3, 8);
        quickUnion.union(6, 5);
        quickUnion.union(9, 4);
        quickUnion.union(1, 2);
        quickUnion.union(5, 6);
        quickUnion.union(1, 6);

        // Assert
        assertTrue(quickUnion.find(8, 9));
        assertTrue(quickUnion.find(1, 6));
        assertFalse(quickUnion.find(0, 9));
    }
}