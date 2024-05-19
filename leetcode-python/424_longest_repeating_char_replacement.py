# Solution:
# 1. Create a sliding window bounded by left and right pointer
# 2. Create a freq table of the elements in the window
# 3. While window is not valid (window_size - max_freq > k) i.e. num of characters to be replaced >= k, move the left pointer and update the freq table
# 4. Keep track of the longest window(subs).


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq_table = {}
        left = 0
        longest_subs = 0

        for right in range(n):
            freq_table[s[right]] = freq_table.get(s[right], 0) + 1
            max_freq = max(freq_table.values())
            window_size = right - left + 1

            while left < right and window_size - max_freq > k:
                freq_table[s[left]] -= 1
                left += 1
                window_size -= 1

            longest_subs = max(window_size, longest_subs)

            # print(
            #     f"left = {left}, right = {right}, window_size = {window_size}, max_freq = {max_freq}, freq_table = {freq_table}, longest_subs = {longest_subs}"
            # )
        return longest_subs


if __name__ == "__main__":
    sol = Solution()

    s = "ABAB"
    k = 2
    res = sol.characterReplacement(s, k)
    print(f"s = {s}, k={k}, res = {res}")

    s = "AABABBA"
    k = 1
    res = sol.characterReplacement(s, k)
    print(f"s = {s}, k={k}, res = {res}")

    s = "ABAA"
    k = 0
    res = sol.characterReplacement(s, k)
    print(f"s = {s}, k={k}, res = {res}")
