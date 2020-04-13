package com.arpan.dsa.datastructures.graphs;

import com.arpan.dsa.exceptions.GraphVertexDosNotExistException;

import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;
import java.util.concurrent.LinkedBlockingDeque;
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

    // This is required to cover any remaining vertices that are not reachable via given source
    // vertex
    for (int i = 0; i < this.numVertices; i++) {
      if (!visited[i]) {
        depthFirstTraversalUtil(i, visited);
      }
    }
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

  @Override
  public boolean isCyclic() {
    // Create visited and isVertexPartOfRecursionStack arrays and initialize with false
    boolean[] visited = new boolean[this.numVertices];
    boolean[] isVertexPartOfRecursionStack = new boolean[this.numVertices];

    // Perform BFS from each vertex.If isCyclicUtil() returns true, for any index there is a cycle.
    for (int i = 0; i < this.numVertices; i++) {
      if (isCyclicUtil(i, visited, isVertexPartOfRecursionStack)) {
        return true;
      }
    }
    return false;
  }

  private boolean isCyclicUtil(
      int currentVertex, boolean[] visited, boolean[] isVertexInRecursionStack) {

    // If vertex is also in the recursion stack, we are visiting it again and there is a cycle
    // present.
    if (isVertexInRecursionStack[currentVertex]) return true;

    // If vertex is already visited, no need to visit
    if (visited[currentVertex]) return false;

    // Mark this vertex visited and a part of recursion stack
    visited[currentVertex] = true;
    isVertexInRecursionStack[currentVertex] = true;

    // Recursively perform DFS on its neighbours and check for cycle
    for (int neighbour : this.adjListArray[currentVertex]) {
      if (isCyclicUtil(neighbour, visited, isVertexInRecursionStack)) return true;
    }

    // Remove current vertex from recursion stack, as we are done visiting.
    isVertexInRecursionStack[currentVertex] = false;

    return false;
  }

  @Override
  public void performTopologicalSort() {
    // Mark all vertices as not visited
    boolean[] visited = new boolean[this.numVertices];

    // Initialize stack
    Deque<Integer> recursionStack = new LinkedBlockingDeque<>();

    // Call topologicalSortUtil() for all vertices which are not yet visited
    for (int vertex = 0; vertex < this.numVertices; vertex++) {
      if (!visited[vertex]) {
        topologicalSortUtil(vertex, visited, recursionStack);
      }
    }

    // Print the topological sort
    System.out.println("Topological sorting of given graph:");
    while (!recursionStack.isEmpty()) {
      System.out.print(recursionStack.pop() + ", ");
    }
    System.out.println();
  }

  private void topologicalSortUtil(
      int currentVertex, boolean[] visited, Deque<Integer> recursionStack) {
    // Mark the current vertex as visited
    visited[currentVertex] = true;

    // Iterate through all neighbours of current vertex
    for (int neighbour : this.adjListArray[currentVertex]) {
      // If neighbour is not visited
      if (!visited[neighbour]) {
        // Recursively traverse its neighbours
        topologicalSortUtil(neighbour, visited, recursionStack);
      }
    }

    // Push the current vertex to the recursion stack
    recursionStack.push(currentVertex);
  }
}
