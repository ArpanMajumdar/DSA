from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        SUDOKU_SIZE = 9
        row_freq = [[0 for _ in range(9)] for _ in range(SUDOKU_SIZE)]
        col_freq = [[0 for _ in range(9)] for _ in range(SUDOKU_SIZE)]
        box_freq = [[0 for _ in range(9)] for _ in range(SUDOKU_SIZE)]

        for i in range(SUDOKU_SIZE):
            for j in range(SUDOKU_SIZE):
                if board[i][j] != ".":
                    digit = int(board[i][j]) - 1
                    row_freq[i][digit] += 1
                    col_freq[j][digit] += 1
                    subbox_idx = self._get_subbox_index(i, j)
                    box_freq[subbox_idx][digit] += 1

                    if (
                        row_freq[i][digit] > 1
                        or col_freq[j][digit] > 1
                        or box_freq[subbox_idx][digit] > 1
                    ):
                        return False

        return True

    def _get_subbox_index(self, row, col):
        return (row // 3) * 3 + (col // 3)

    def isValidSudokuUsingSet(self, board: List[List[str]]) -> bool:
        SUDOKU_SIZE = 9
        row_freq = [set() for _ in range(SUDOKU_SIZE)]
        col_freq = [set() for _ in range(SUDOKU_SIZE)]
        box_freq = [set() for _ in range(SUDOKU_SIZE)]

        for i in range(SUDOKU_SIZE):
            for j in range(SUDOKU_SIZE):
                digit = board[i][j]
                if digit != ".":
                    if digit in row_freq[i]:
                        return False
                    else:
                        row_freq[i].add(digit)

                    if digit in col_freq[j]:
                        return False
                    else:
                        col_freq[j].add(digit)

                    subbox_idx = self._get_subbox_index(i, j)
                    if digit in box_freq[subbox_idx]:
                        return False
                    else:
                        box_freq[subbox_idx].add(digit)

        return True


if __name__ == "__main__":
    sol = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    valid_sudoku = sol.isValidSudoku(board)
    print(f"board = {board}, valid_sudoku = {valid_sudoku}")

    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    valid_sudoku = sol.isValidSudoku(board)
    print(f"board = {board}, valid_sudoku = {valid_sudoku}")
