def is_palindrome(s):
    n = len(s)
    start, end = 0, n - 1

    while start < end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            return palindrome(s, start, end - 1) or palindrome(s, start + 1, end)
        
    return True


def palindrome(s, start, end):
    while start < end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            return False
    return True


if __name__ == "__main__":
    inputs = [
        "abbababa",
        "raceacat",
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVgVUTSRQPONMLKLJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba",
    ]

    for input in inputs:
        sol = is_palindrome(input)
        print(f"input: {input}, sol = {sol}")
