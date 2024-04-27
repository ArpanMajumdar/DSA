class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index = {}
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in index:
                return [i, index[diff]]
            else:
                index[nums[i]] = i

        return []


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    res = sol.twoSum(nums, target)
    print(f"nums = {nums}, target = {target}, result = {res}")

    nums = [3, 2, 4]
    target = 6
    res = sol.twoSum(nums, target)
    print(f"nums = {nums}, target = {target}, result = {res}")
