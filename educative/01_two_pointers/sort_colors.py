# Solution
# Declare 3 pointers: start = 0, current = 0, end = len(arr) - 1
# If arr[current] = 0, swap with arr[start]. current++, start++
# If arr[current] = 1, current++
# If arr[current] = 2, swap with arr[end], end--

# Idea:
# [0, 0, 0, ..., 0, 1, 1, ..., 1, 2, 2, ..., 2]
# The essence of the algorithm lies in efficiently partitioning the array into three sections corresponding to the colors 0, 1, and 2.
# We keep track of the boundaries of the 0 and 2 sections while iterating through the array. 0's are kept on the left side of the array, while 2's remain on the right side, with whites in between.
# start pointer always points to the element just after 0's
# end pointer always points to the element just before 2's
# current pointer goes through the middle unsorted array and sorts it


def sort_colors(colors: list[int]) -> list[int]:
    n = len(colors)
    start = 0
    current = 0
    end = n - 1

    while current <= end:
        if colors[current] == 0:
            swap(colors, current, start)
            start += 1
            current += 1

        elif colors[current] == 1:
            current += 1
        else:
            swap(colors, current, end)
            end -= 1

    return colors


def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


if __name__ == "__main__":
    inputs = [
        [2, 2, 1, 1, 0],
        [2, 2, 0, 1, 2, 2, 0, 2],
        [0, 0, 1, 0, 1, 1, 1, 2, 1, 2],
        [0, 1, 0],
    ]
    for colors in inputs:
        print(f"colors = {colors}")
        sort_colors(colors)
        print(f"sorted colors = {colors}")
        print()
