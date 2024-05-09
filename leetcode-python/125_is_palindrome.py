class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s.lower()))

        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1

        return True


if __name__ == "__main__":
    sol = Solution()
    s = "0P"
    res = sol.isPalindrome(s)
    print(f"Input: {s}")
    print(f"Outpt: {res}")
