import re

# Solution
# 1. Reverse the entire sentence
# 2. Reverse each word individually
# 2.1 Use two pointers: start and end. start marks the beginning of a word and end marks the end of the word.
# 2.2 When word boundary is found, we reverse the word in place
# 2.3 After reversing, move the start and end to the beginning of the next word
# 2.4 Repeat the processs

# Time complexity
# It takes O(n) time to trim the string and array is traversed twice by start and end pointers.

# Space complexity
# No extra space is needed. However, since strings are immutable in Python, we need to convert it to a list. So, space complexity is O(n).


def reverse_words(sentence: str) -> str:
    sentence = sentence.strip()
    sentence = re.sub(pattern=" +", repl=" ", string=sentence)
    n = len(sentence)
    sentence_list = list(sentence)
    reverse(sentence_list, 0, n - 1)

    start, end = 0, 0
    for end in range(0, n):
        if end == n - 1 or sentence_list[end] == " ":
            if end == n - 1:
                reverse(sentence_list, start, end)
            else:
                reverse(sentence_list, start, end - 1)
            start = end + 1

    return "".join(sentence_list)


def reverse(sentence_list: list, start: int, end: int):
    while start < end:
        temp = sentence_list[start]
        sentence_list[start] = sentence_list[end]
        sentence_list[end] = temp
        start += 1
        end -= 1


if __name__ == "__main__":
    input = "We love Python"
    print(reverse_words(input))
