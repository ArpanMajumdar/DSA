# Problem
# Given two strings, s and t, find the minimum window substring in s, which has the following properties:
# 1. It is the shortest substring of s that includes all of the characters present in t.
# 2. It must contain at least the same frequency of each character as in t.
# 3. The order of the characters does not matter here.
# Constraints: Strings s and t consist of uppercase and lowercase English characters.

# Solution
# 1. Initialize two hash maps: t_freq_map to store the character frequency counts of string t and curr_window_freq_map to store the char frequency
# 2. Iterate over s using a sliding window with start and end pointers and perform the following steps
#   2.1 If current char is in t, update its frequency in curr_window_freq_map
#   2.2 Check if the freq of all the chars in curr_window_freq_map >= freq of all the chars in t_freq_map. Keep shrinking the window until this condition holds true.
#   2.3 Keep track of the min_window_len for which the condition is true. If we get a smaller window, then update the min_window_len and min_window_substr
# 3. Return the minimum window substring

# Time complexity: O(m+n)
# Space complexity: O(1) because s and t consist of only upper and lowercase alphabets, the maximum size of maps can be 52.


def min_window(s: str, t: str) -> str:
    s_len = len(s)
    if len(s) < 1 or len(t) < 1:
        return ""

    # Create freq table for t
    t_freq_map = {}
    curr_window_freq_map = {}
    for i in t:
        curr_window_freq_map[i] = 0
        t_freq_map[i] = t_freq_map.get(i, 0) + 1

    start = 0
    min_window_len = float("inf")
    min_window_substr = ""
    curr_window_len = 0

    # Sliding window
    for end in range(s_len):
        if s[end] in t_freq_map:
            curr_window_freq_map[s[end]] = curr_window_freq_map.get(s[end], 0) + 1

        # Shink the sliding window till s_freq has all the elements >= t_freq elements
        while check_freq(curr_window_freq_map, t_freq_map):
            curr_window_len = end - start + 1
            if curr_window_len < min_window_len:
                min_window_len = curr_window_len
                min_window_substr = s[start : end + 1]

            if s[start] in t_freq_map:
                curr_window_freq_map[s[start]] -= 1
            start += 1

    return min_window_substr


def check_freq(s_freq_map: dict[str, int], t_freq_map: dict[str, int]) -> bool:
    for ch, freq in t_freq_map.items():
        if ch not in s_freq_map or s_freq_map[ch] < freq:
            return False
    return True


if __name__ == "__main__":
    inputs = [
        {"s": "cabwefgewcwaefgcf", "t": "cae"},
        {"s": "bbaac", "t": "aba"},
        {"s": "AbabbbAbaA", "t": "Bab"},
    ]

    for input in inputs:
        output = min_window(input["s"], input["t"])
        print(f"s = {input['s']}, t = {input['t']}")
        print(f"output = {output}")
        print()
