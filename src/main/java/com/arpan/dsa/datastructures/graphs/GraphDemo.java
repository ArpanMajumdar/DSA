package com.arpan.dsa.datastructures.graphs;

public class GraphDemo {

  public static void main(String[] args) {
    // Create a graph with adjacency list implementation
    Graph graph = new GraphWithAdjListImpl(4);
//    graph.addUndirectedEdge(0, 1);
//    graph.addUndirectedEdge(0, 4);
//    graph.addUndirectedEdge(1, 2);
//    graph.addUndirectedEdge(1, 3);
//    graph.addUndirectedEdge(1, 4);
//    graph.addUndirectedEdge(2, 3);
//    graph.addUndirectedEdge(3, 4);
//
//    graph.print();
//    graph.performBreadthFirstTraversal(0);

    graph.addDirectedEdge(0, 1);
    graph.addDirectedEdge(0, 2);
    graph.addDirectedEdge(1, 2);
    graph.addDirectedEdge(2, 0);
    graph.addDirectedEdge(2, 3);
    graph.addDirectedEdge(3, 3);

    graph.print();
//    graph.performBreadthFirstTraversal(2);
    graph.performDepthFirstTraversal(2);
  }
}
