from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,3,4]
        # [1,2,6,24]
        # [24,24,12,4]

        n = len(nums)
        answer = [0 for _ in range(n)]
        zero_indices = self.indices_with_zeros(nums)

        if len(zero_indices) > 1:
            return answer
        elif len(zero_indices) == 1:
            product = 1
            for i, num in enumerate(nums):
                if i != zero_indices[0]:
                    product *= num

            answer[zero_indices[0]] = product
            return answer

        else:
            left_to_right_cumsum = [0 for _ in range(n)]
            right_to_left_cumsum = [0 for _ in range(n)]
            left_to_right_cumsum[0] = nums[0]
            right_to_left_cumsum[n - 1] = nums[n - 1]

            for i in range(n - 1):
                left_to_right_cumsum[i + 1] = nums[i + 1] * left_to_right_cumsum[i]

            for i in range(n - 1, 0, -1):
                right_to_left_cumsum[i - 1] = nums[i - 1] * right_to_left_cumsum[i]

            for i in range(n):
                if i == 0:
                    answer[i] = right_to_left_cumsum[i + 1]
                elif i == n - 1:
                    answer[i] = left_to_right_cumsum[i - 1]
                else:
                    answer[i] = (
                        left_to_right_cumsum[i - 1] * right_to_left_cumsum[i + 1]
                    )
            return answer

    def indices_with_zeros(self, nums):
        zero_indices = []
        for i, num in enumerate(nums):
            if num == 0:
                zero_indices.append(i)
        return zero_indices

    # This solution uses the same result array for memoization of left and right instead of using two arrays. 
    def productExceptSelfOptimized(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        left_cumproduct = 1
        for i in range(n):
            result[i] = left_cumproduct
            left_cumproduct *= nums[i]

        right_cumproduct = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_cumproduct
            right_cumproduct *= nums[i]

        return result


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4, 5]
    answer = sol.productExceptSelfOptimized(nums)
    print(f"nums = {nums}, answer = {answer}")

    # nums = [-1, 1, 0, -3, 3]
    # answer = sol.productExceptSelf(nums)
    # print(f"nums = {nums}, answer = {answer}")
