# Solution

# 1. Sort the array
# 2. Loop through the entire array. In each iteration
# 3 Fix the current array element as the first element of triplet. Use two pointers approach to find the other two elements of the triplet
# 4. Calculate the triplet sum.
# 4.1 If triplet sum = target, return True
# 4.2 If triplet sum < target, move left pointer by 1
# 4.3 If triplet sum > target, move right pointer by 1

# Time comlexity
# Sorting the array: n.log(n)
# Nested for loop: n^2
# Total complexity = O(nlog(n) + n^2) = O(n^2)

# Space complexity
# Space complexity of built-in Python sort function: O(n)


def find_sum_of_three(nums: list[int], target: int) -> bool:
    sorted_nums = sorted(nums)
    n = len(sorted_nums)

    for i in range(0, n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            triplet_sum = sorted_nums[left] + sorted_nums[i] + sorted_nums[right]

            if triplet_sum == target:
                return True
            elif triplet_sum < target:
                left += 1
            else:
                right -= 1

    return False


if __name__ == "__main__":
    inputs = [
        ([1, -1, 0], -1),
        ([3, 7, 1, 2, 8, 4, 5], 20),
        ([-1, 2, 1, 4], 1),
        ([-1, 2, 1, 4, -2], 1),
        ([8, 2, 4, 9, 5], 17),
    ]

    for nums, target in inputs:
        sol = find_sum_of_three(nums, target)
        print(f"nums = {nums}, target = {target}, find_sum_of_three = {sol}")
