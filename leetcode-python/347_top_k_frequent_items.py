import heapq

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Create freq table
        freq_table = {}
        for num in nums:
            freq_table[num] = freq_table.get(num, 0) + 1

        # Sort the freq table by freq in descending order
        sorted_freq_table = sorted(freq_table.items(), key=lambda x: x[1], reverse=True)
        top_k_nums = []

        # Take the top k nums
        for i in range(k):
            top_k_nums.append(sorted_freq_table[i][0])

        return top_k_nums

    def topKFrequentUsingHeap(self, nums: list[int], k: int) -> list[int]:
        # Create freq table
        freq_table = {}
        for num in nums:
            freq_table[num] = freq_table.get(num, 0) + 1

        # Create a heap using the freq as key. Extract k largest items from heap.
        top_k_items = heapq.nlargest(k, freq_table.items(), key=lambda x: x[1])
        return [item[0] for item in top_k_items]


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    res = sol.topKFrequentUsingHeap(nums, k)
    print(f"nums = {nums}, k = {k}, result = {res}")
