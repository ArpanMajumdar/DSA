package com.arpan.dsa.datastructures.graphs.problems.connected_components;

public class ConnectedComponents {
  private int[][] matrix;
  private int totalRows;
  private int totalCols;

  public ConnectedComponents(int[][] matrix) {
    this.matrix = matrix;
    this.totalRows = matrix[0].length;
    this.totalCols = matrix.length;
  }

  public int findNumOfConnectedComponents() {
    boolean[][] visited = new boolean[totalRows][totalCols];

    int numOfConnectedComponents = 0;
    int[] rowOffsets = {-1, -1, -1, 0, 0, 1, 1, 1};
    int[] colOffsets = {-1, 0, 1, -1, 1, -1, 0, 1};

    for (int i = 0; i < totalRows; i++) {
      for (int j = 0; j < totalCols; j++) {
        if (this.matrix[i][j] == 1 && !visited[i][j]) {
          performDepthFirstTraversal(i, j, rowOffsets, colOffsets, visited);
          numOfConnectedComponents++;
        }
      }
    }
    return numOfConnectedComponents;
  }

  private void performDepthFirstTraversal(
      int rowNum, int colNum, int[] rowOffsets, int[] colOffsets, boolean[][] visited) {
    visited[rowNum][colNum] = true;
    int adjRow, adjCol;

    for (int k = 0; k < 8; k++) {
      adjRow = rowNum + rowOffsets[k];
      adjCol = colNum + colOffsets[k];
      if (isEligibleForDfs(adjRow, adjCol, visited)) {
        performDepthFirstTraversal(adjRow, adjCol, rowOffsets, colOffsets, visited);
      }
    }
  }

  private boolean isEligibleForDfs(int rowNum, int colNum, boolean[][] visited) {
    return rowNum >= 0
        && rowNum < this.totalRows
        && colNum >= 0
        && colNum < this.totalCols
        && this.matrix[rowNum][colNum] == 1
        && !visited[rowNum][colNum];
  }
}
