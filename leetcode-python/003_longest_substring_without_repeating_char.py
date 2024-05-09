class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substr = 0

        i, j = 0, 0
        n = len(s)
        char_set = set()
        curr_substr = 0

        while i < n and j < n:

            while j < n and s[j] not in char_set:
                print(f"while 1: i = {i}, j = {j}")
                char_set.add(s[j])
                curr_substr += 1
                j += 1

            # Update the longest substring length
            longest_substr = max(curr_substr, longest_substr)
            print(f"i = {i}, j = {j}")

            # Move the left pointer just after the repeating character
            while i < n and j < n and i < j and s[i] != s[j]:
                print(f"while 2: i = {i}, j = {j}")
                char_set.remove(s[i])
                curr_substr -= 1
                i += 1

            if j < n:
                char_set.remove(s[j])
                curr_substr -= 1
            i += 1

        return longest_substr


if __name__ == "__main__":
    sol = Solution()
    # s = "abcabcbb"
    # res = sol.lengthOfLongestSubstring(s)
    # print(f"s = {s}")
    # print(f"res = {res}")

    s = "dvdf"
    res = sol.lengthOfLongestSubstring(s)
    print(f"s = {s}")
    print(f"res = {res}")
