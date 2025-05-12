# Problem
# Given an array of positive integers, nums, and a positive integer, target, find the minimum length of a contiguous subarray whose sum is greater than or equal to the target. If no such subarray is found, return 0.
# Constraints
# 1 <= target <= 10^4
# 1 <= len(nums) <= 10^3
# 1 <= nums[i] <= 10^3

# Solution
# 1. Intialize: min_window_size = inf, window_sum = 0
# 2. Traverse the array using sliding window approach.
# 3. Expand the window until the window sum is less than target.
# 4. Shrink the window to reduce the window size while window sum >= target.

# Time complexity: O(n)
# Space complexity: O(1)


def min_sub_array_len(target: int, nums: list[int]) -> int:
    n = len(nums)
    min_window_size = float("inf")
    window_sum = 0
    start = 0

    if sum(nums) < target:
        return 0

    for end in range(n):
        window_sum += nums[end]
        # print(f"start = {start}, end = {end}, window_sum = {window_sum}, min_window_size = {min_window_size}")

        while window_sum >= target:
            min_window_size = min(min_window_size, end - start + 1)
            window_sum -= nums[start]
            start += 1

    if min_window_size == float("inf"):
        min_window_size = 0

    return min_window_size


if __name__ == "__main__":
    inputs = [
        {"nums": [2, 3, 1, 2, 4, 3], "target": 7},
        {"nums": [1, 1, 1, 1, 1, 3], "target": 11},
        {"nums": [1, 2, 7, 3, 4, 5], "target": 10},
    ]

    for input in inputs:
        output = min_sub_array_len(input["target"], input["nums"])
        print(f"nums = {input['nums']}, target = {input['target']}")
        print(f"output = {output}")
        print()
