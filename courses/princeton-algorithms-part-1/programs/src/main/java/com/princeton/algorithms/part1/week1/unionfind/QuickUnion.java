package com.princeton.algorithms.part1.week1.unionfind;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class QuickUnion implements UnionFind {

    private static final Logger LOGGER = LoggerFactory.getLogger(QuickUnion.class);
    private final int[] id;

    public QuickUnion(int N) {
        id = new int[N];
        for (int i = 0; i < N; i++) {
            id[i] = i;
        }
    }

    @Override
    public void union(int p, int q) {
        int rootp = root(p);
        int rootq = root(q);

        makeParent(rootp, rootq);
    }

    @Override
    public boolean find(int p, int q) {
        return root(p) == root(q);
    }

    private int parent(int i) {
        return id[i];
    }

    private int root(int i) {
        while (i != parent(i)) {
            i = parent(i);
        }
        return i;
    }

    private void makeParent(int child, int parent) {
        id[child] = parent;
    }

    private String printIdArray() {
        StringBuilder buffer = new StringBuilder();
        for (int value : id) {
            buffer.append(value).append("\t");
        }
        buffer.append("\n");
        return buffer.toString();
    }
}
