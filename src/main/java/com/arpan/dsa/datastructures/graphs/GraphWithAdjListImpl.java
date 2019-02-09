package com.arpan.dsa.datastructures.graphs;

import com.arpan.dsa.exceptions.GraphVertexDosNotExistException;

import java.util.LinkedList;
import java.util.Queue;
import java.util.concurrent.LinkedBlockingQueue;

public class GraphWithAdjListImpl implements Graph {

  private int numVertices;
  private LinkedList<Integer> adjListArray[];

  public GraphWithAdjListImpl(int numVertices) {
    this.numVertices = numVertices;
    this.adjListArray = new LinkedList[numVertices];

    // Initialize each vertex with empty Linked List
    for (int i = 0; i < numVertices; i++) {
      this.adjListArray[i] = new LinkedList<>();
    }
  }

  @Override
  public void addUndirectedEdge(int src, int dest) {
    this.adjListArray[src].add(dest);
    this.adjListArray[dest].add(src);
  }

  @Override
  public void addDirectedEdge(int src, int dest) {
    this.adjListArray[src].add(dest);
  }

  @Override
  public void print() {
    for (int i = 0; i < numVertices; i++) {
      System.out.print("Vertex " + i + " : ");
      this.adjListArray[i].stream().forEach(vertex -> System.out.print(vertex + ", "));
      System.out.println();
    }
  }

  @Override
  public void performBreadthFirstTraversal(int src) {

    if (src < 0 || src >= this.numVertices) {
      throw new GraphVertexDosNotExistException(
          src + " is not a valid vertex for the given graph.");
    }

    boolean[] visited = new boolean[this.numVertices];
    Queue<Integer> neighbours = new LinkedBlockingQueue<>();
    int currentVertex;

    // Push source vertex to queue
    neighbours.offer(src);

    // Mark the source vertex as visited
    visited[src] = true;

    System.out.println("Performing breadth first traversal starting from vertex " + src);
    // While queue is not empty
    while (!neighbours.isEmpty()) {
      // Dequeue one vertex from queue and print
      currentVertex = neighbours.poll();

      System.out.print(currentVertex + ", ");

      // Iterate through all the neighbours of current vertex
      for (int neighbour : this.adjListArray[currentVertex]) {
        // If that neighbour is not visited, push it to queue and mark it as visited
        if (!visited[neighbour]) {
          visited[neighbour] = true;
          neighbours.offer(neighbour);
        }
      }
    }
  }

  @Override
  public void performDepthFirstTraversal(int src) {
    boolean[] visited = new boolean[this.numVertices];
    System.out.println("Performing depth first traversal starting from vertex " + src);
    depthFirstTraversalUtil(src, visited);
  }

  private void depthFirstTraversalUtil(int currentVertex, boolean[] visited) {
    // Mark the current vertex as visited and print it
    visited[currentVertex] = true;
    System.out.print(currentVertex + ", ");

    // Iterate through all neighbours of current vertex
    for (int neighbour : this.adjListArray[currentVertex]) {
      // If neighbour is not visited
      if (!visited[neighbour]) {
        // Recursively traverse its neighbours
        depthFirstTraversalUtil(neighbour, visited);
      }
    }
  }
}
