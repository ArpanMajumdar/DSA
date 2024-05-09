from typing import List

# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Example 2:

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
# Example 3:

# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            cur_sum = numbers[i] + numbers[j]

            if cur_sum == target:
                return [i + 1, j + 1]
            elif cur_sum < target:
                i += 1
            else:
                j -= 1
        return []


if __name__ == "__main__":
    sol = Solution()

    numbers = [2, 7, 11, 15]
    target = 9
    res = sol.twoSum(numbers, target)
    print(f"Input: numbers = {numbers}, target = {target}")
    print(f"Output: {res}")

    numbers = [2, 3, 4]
    target = 6
    res = sol.twoSum(numbers, target)
    print(f"Input: numbers = {numbers}, target = {target}")
    print(f"Output: {res}")
