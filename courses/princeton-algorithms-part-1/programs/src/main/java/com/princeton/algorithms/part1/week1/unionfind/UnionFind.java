package com.princeton.algorithms.part1.week1.unionfind;

public interface UnionFind {
    void union(int p, int q);

    boolean find(int p, int q);
}
