class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq_table = {}
        s2_freq_table = {}

        for char in s1:
            s1_freq_table[char] = s1_freq_table.get(char, 0) + 1

        left = 0

        for i in range(len(s2) - len(s1) + 1):
            left = i
            right = i + len(s1) - 1

            if i == 0:
                for j in range(left, right + 1):
                    s2_freq_table[s2[j]] = s2_freq_table.get(s2[j], 0) + 1
            else:
                s2_freq_table[s2[left - 1]] -= 1
                s2_freq_table[s2[right]] = s2_freq_table.get(s2[right], 0) + 1

            s2_freq_table = {k: v for k, v in s2_freq_table.items() if v != 0}
            print(
                f"left = {left}, right={right}, s1_freq_table = {s1_freq_table}, s2_freq_table = {s2_freq_table}"
            )
            if s1_freq_table == s2_freq_table:
                return True

        return False


if __name__ == "__main__":
    sol = Solution()

    # s1 = "ab"
    # s2 = "eidbaooo"
    # res = sol.checkInclusion(s1, s2)
    # print(f"s1 = {s1}, s2 = {s2}, res = {res}")

    s1 = "adc"
    s2 = "dcda"
    res = sol.checkInclusion(s1, s2)
    print(f"s1 = {s1}, s2 = {s2}, res = {res}")
