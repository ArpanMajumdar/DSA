
def longest_repeating_character_replacement(s: str, k: int) -> int:
    n = len(s)
    longest_substr_len = 0
    start = 0
    freq_map = {}

    for end in range(n):
        freq_map[s[end]] = freq_map.get(s[end], 0) + 1
        window_size = end - start + 1
        max_freq = find_max_freq(freq_map)

        if window_size - max_freq <= k:
            longest_substr_len = max(longest_substr_len, window_size)
        else:
            freq_map[s[start]] -= 1
            start += 1

    return longest_substr_len


def find_max_freq(freq_map: dict):
    return max(freq_map.values())


if __name__ == "__main__":
    inputs = [{"s": "aabccbb", "k": 2},
              {"s": "fzfzfz", "k": 6},
              {"s": "xxxxx", "k": 1},
              {"s": "lmno", "k": 2},
              {"s": "n", "k":0}]

    for input in inputs:
        output = longest_repeating_character_replacement(input["s"], input["k"])
        print(f"s = {input["s"]}, k = {input["k"]}")
        print(f"output = {output}")
        print()
