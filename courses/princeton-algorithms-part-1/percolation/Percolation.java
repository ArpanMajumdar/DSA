/* *****************************************************************************
 *  Name:    Arpan Majumdar
 *  NetID:   arpanmajumdar
 *  Precept: P00
 *
 *  Description:  Monte carlo simulation for 2-D Percolation Problem
 **************************************************************************** */

import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {

    private int size; // Size of lattice
    private boolean[][] lattice; // Boolean 2-D array to keep track of open sites
    private WeightedQuickUnionUF unionFind; // Union find data structure
    private int numOpenSites; // Keeps track of number of sites opened
    private int topIndex;
    private int bottomIndex;

    // creates n-by-n grid, with all sites initially blocked
    public Percolation(int n) {
        this.size = n;
        this.lattice = new boolean[n][n];
        this.unionFind = new WeightedQuickUnionUF((size * size) + 2);
        this.numOpenSites = 0;
        this.topIndex = size * size;
        this.bottomIndex = topIndex + 1;
    }

    // opens the site (row, col) if it is not open already
    public void open(int row, int col) {
        checkIfValid(row, col);
        if (!lattice[row - 1][col - 1]) {
            int[] rowIndices = { 0, 0, 1, -1 };
            int[] colIndices = { -1, 1, 0, 0 };

            int centerIndex = get1DIndex(row, col);
            for (int i = 0; i < 4; i++) {
                int neighbourRowIndex = row + rowIndices[0];
                int neighbourColIndex = col + colIndices[0];

                if (isValid(neighbourRowIndex, neighbourColIndex) &&
                        isOpen(neighbourRowIndex, neighbourColIndex)) {
                    int neighbourIndex = get1DIndex(neighbourRowIndex,
                                                    neighbourColIndex);
                    unionFind.union(centerIndex, neighbourIndex);
                    if (row == 1 && isOpen(row, col)) {
                        unionFind.union(topIndex, centerIndex);
                    }
                    if (row == size - 1 && isOpen(row, col)) {
                        unionFind.union(bottomIndex, col);
                    }
                }
            }
            numOpenSites++;
            lattice[row - 1][col - 1] = true;
        }
    }

    // Returns true if index is valid, false otherwise
    private boolean isValid(int row, int col) {
        return row < 1 || row > size || col < 1 || col > size;
    }

    // Throws exception if index is invalid
    private void checkIfValid(int row, int col) {
        if (isValid(row, col))
            throw new IllegalArgumentException(
                    "Row and col should be between 1 and " + size);
    }

    // is the site (row, col) open?
    public boolean isOpen(int row, int col) {
        checkIfValid(row, col);
        return lattice[row - 1][col - 1];
    }

    // is the site (row, col) full?
    public boolean isFull(int row, int col) {
        int index = get1DIndex(row, col);
        int rootSite = unionFind.find(index);
        int rootTop = unionFind.find(topIndex);
        return rootSite == rootTop;
    }

    // returns the number of open sites
    public int numberOfOpenSites() {
        return numOpenSites;
    }

    // does the system percolate?
    public boolean percolates() {
        int rootTop = unionFind.find(topIndex);
        int rootBottom = unionFind.find(bottomIndex);
        return rootBottom == rootTop;
    }

    // Get 1-D index corresponsing to 2-D indices
    private int get1DIndex(int i, int j) {
        return (i - 1) * size + (j - 1);
    }

    // Main
    public static void main(String[] args) {
        int row, col;
        int[] openSiteIndex;
        char answer;

        System.out.println("Enter size of lattice:");
        int size = StdIn.readInt();
        Percolation percolation = new Percolation(size);

        do {
            System.out.println("Enter row and col:");
            row = StdIn.readInt();
            col = StdIn.readInt();

            percolation.open(row + 1, col + 1);

            System.out.println("Do you want to continue?(y/n)");
            StdIn.readChar();
            answer = StdIn.readChar();
        } while (answer != 'n');

        if (percolation.percolates()) {
            System.out.println("System percolates");
        }
        else {
            System.out.println("System does not percolate");
        }
    }
}
