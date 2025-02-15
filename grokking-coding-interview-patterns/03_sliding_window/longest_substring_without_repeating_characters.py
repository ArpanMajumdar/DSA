# Problem: Given a string, input_str, return the length of the longest substring without repeating characters.
# Constraints:
#   - 1 <= len(input_str) <= 10^5
#   - input_str consists of English letters, digits, symbols, and spaces.

# Solution
# 1. Traverse the string using the sliding window approach with start and end pointers
# 2. Create a hash map char_idx_map to store the characters and their indices in the string
#   2.1 If the current char is not present in the map or it is present but it's outside the current window, update the character's index in the map.
#   2.2 If the current char repeats within the current window, calculate the current window length current_window_len = end - start. Update the longest_window_len if current_window_len is greater then the previous longest window.
#   2.3 Move the start pointer to one character after the repeating character.
# 3. Handle the case if the longest window is at the end of the string. In this case, current_window_len = end - start + 1.

# Time complexity: O(n)
# Space complexity: O(1) because constant space is required for hashmap which is equal to the number of distinct characters.


def find_longest_substring(input_str: str) -> int:
    n = len(input_str)
    char_idx_map = {}
    start = 0
    longest_window_len = 0

    for end in range(n):
        # window = input_str[start:end+1]
        # print(f"start={start}, end = {end}, window = {window}, longest_window_len = {longest_window_len}, char_idx_map = {char_idx_map}")
        if input_str[end] not in char_idx_map or (
            input_str[end] in char_idx_map and char_idx_map[input_str[end]] < start
        ):  # character is not repeating in current window
            char_idx_map[input_str[end]] = end
        else:  # character is repeating in current window
            current_window_len = end - start
            longest_window_len = max(current_window_len, longest_window_len)
            start = char_idx_map[input_str[end]] + 1
            char_idx_map[input_str[end]] = end

        # Handle the case when longest window is at the end of the string
        if end == n - 1:
            current_window_len = end - start + 1
            longest_window_len = max(current_window_len, longest_window_len)

    return longest_window_len


if __name__ == "__main__":
    inputs = [
        {"input_str": "conceptoftheday"},
        {"input_str": "bbbbbbbbbbbbbbbb"},
        {"input_str": "racecar"},
        {"input_str": "bankrupted"},
        {"input_str": "aba"},
    ]

    for input in inputs:
        output = find_longest_substring(input["input_str"])
        print(f"input_str = {input['input_str']}")
        print(f"output = {output}")
        print()
