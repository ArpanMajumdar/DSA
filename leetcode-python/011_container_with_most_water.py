from typing import List

# Key takeaways
# - Use two pointer method
# - Update the pointer that has a smaller height as bottleneck is the side that has a smaller height


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1

        max_area = 0
        area = 0
        while i < j:
            area = self.calc_area(height, i, j)
            # print(f"i = {i}, j = {j}, area = {area}")
            max_area = max(area, max_area)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area

    def calc_area(self, height: List[int], i: int, j: int) -> int:
        return (j - i) * min(height[i], height[j])


if __name__ == "__main__":
    sol = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    res = sol.maxArea(height)
    print(f"height = {height}")
    print(f"res = {res}")

    height = [1, 2, 4, 3]
    res = sol.maxArea(height)
    print(f"height = {height}")
    print(f"res = {res}")

    height = [1, 3, 2, 5, 25, 24, 5]
    res = sol.maxArea(height)
    print(f"height = {height}")
    print(f"res = {res}")
