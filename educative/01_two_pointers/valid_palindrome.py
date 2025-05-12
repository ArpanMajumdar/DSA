# 1. Initialize two pointers at the beginning of the string
# 2. Check whether or not the current pair of characters is identical
# 3. If they are not identical, return False. Otherwise, move both pointers by one index toward the middle
# 4. Keep traversing them toward the middle until they meet
# 5. If we reach the middle without finding a misnatch, return True


def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    inputs = ["racecar", "abab"]

    for input in inputs:
        sol = is_palindrome(input)
        print(f"s = {input}, is_palindrome = {sol}")
