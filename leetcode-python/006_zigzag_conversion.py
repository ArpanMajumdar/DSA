class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s

        rows = ["" for _ in range(numRows)]
        n = len(s)

        row_idx = 0
        direction = 1
        for i in range(n):
            rows[row_idx] += s[i]
            row_idx += direction

            if row_idx == numRows - 1 or row_idx == 0:
                direction = -direction
        return "".join(rows)


if __name__ == "__main__":
    sol = Solution()
    s = "PAYPALISHIRING"
    num_rows = 3
    output = sol.convert(s, num_rows)
    print(f"{s=}, {num_rows=}, {output=}")
