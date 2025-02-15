class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_freq = self.calc_char_freq(s)
        t_freq = self.calc_char_freq(t)
        return s_freq == t_freq

    def calc_char_freq(self, s):
        s_freq = {}
        for char in s:
            if char in s_freq:
                s_freq[char] += 1
            else:
                s_freq[char] = 1
        return s_freq


if __name__ == "__main__":
    sol = Solution()
    s1 = "anagram"
    t1 = "nagaram"
    res1 = sol.isAnagram(s1, t1)
    print(f"s1 = {s1}, t1 = {t1}, Result = {res1}")

    s2 = "rat"
    t2 = "car"
    res2 = sol.isAnagram(s2, t2)
    print(f"s2 = {s2}, t2 = {t2}, Result = {res2}")
