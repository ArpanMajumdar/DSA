package com.arpan.dsa.datastructures.graphs.problems.connected_components;

public class ConnectedComponentsDemo {

  public static void main(String[] args) {
    //
    int[][] matrix = {
      {1, 1, 0, 0, 0}, {0, 1, 0, 0, 1}, {1, 0, 0, 1, 1}, {0, 0, 0, 0, 0}, {1, 0, 1, 0, 1}
    };

    ConnectedComponents connectedComponents=new ConnectedComponents(matrix);
    System.out.println("Number of connected components in given matrix: "+connectedComponents.findNumOfConnectedComponents());
  }
}
