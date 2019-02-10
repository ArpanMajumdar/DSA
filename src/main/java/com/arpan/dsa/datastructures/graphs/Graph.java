package com.arpan.dsa.datastructures.graphs;

public interface Graph {

  void addDirectedEdge(int src, int dest);

  void addUndirectedEdge(int src, int dest);

  void print();

  void performBreadthFirstTraversal(int src);

  void performDepthFirstTraversal(int src);

  boolean isCyclic();

  void performTopologicalSort();
}
