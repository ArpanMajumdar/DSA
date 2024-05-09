from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_seq_len = 1

        for n in nums:
            # Check if the num is start of a sequence i.e. if it doesn't has a left neighbor
            if (n - 1) not in nums_set:
                seq_len = 0

                # Check consecutive nums
                while (n + seq_len) in nums_set:
                    seq_len += 1
                max_seq_len = max(seq_len, max_seq_len)

        return max_seq_len


if __name__ == "__main__":
    sol = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    res = sol.longestConsecutive(nums)
    print(f"nums = {nums}")
    print(f"res = {res}")

    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    res = sol.longestConsecutive(nums)
    print(f"nums = {nums}")
    print(f"res = {res}")
