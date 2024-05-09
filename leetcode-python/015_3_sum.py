from typing import List


def swap(nums: List[int], i: int, j: int):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


def sort_triplet(triplet: List[int]):
    if triplet[0] > triplet[1]:
        swap(triplet, 0, 1)
    if triplet[1] > triplet[2]:
        swap(triplet, 1, 2)
    if triplet[0] > triplet[1]:
        swap(triplet, 0, 1)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        output = set()

        for i, num in enumerate(nums):
            target = -num
            two_sum_result = self.twoSum(nums, target, ignore_idx=i)
            # print(f"i = {i}, num = {num}, two_sum_result = {two_sum_result}")

            if len(two_sum_result) > 0:
                triplet = [nums[i]] + two_sum_result
                sort_triplet(triplet)
                output.add(tuple(triplet))

        return [list(tp) for tp in output]

    def twoSum(self, numbers: List[int], target: int, ignore_idx: int) -> List[int]:
        numbers_set = set([num for i, num in enumerate(numbers) if i != ignore_idx])
        return []


if __name__ == "__main__":
    sol = Solution()
    nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    res = sol.threeSum(nums)
    print(f"Input: nums = {nums}")
    print(f"Output: {res}")
