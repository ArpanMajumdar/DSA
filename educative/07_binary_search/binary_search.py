# Steps
# 1. Find the middle element in a sorted array
# 2. Compare the middle element with the target element. If it matches, return the index of the element
# 3. If target element is smaller than the middle element, search the left half of array. Otherwise, search the right half of the array
# 4. Repeat until target value is found. Return -1 if not found.


def binary_search(nums: list[int], target: int):
    start, end = 0, len(nums) - 1
    if target < nums[0] or target > nums[end]:
        return -1

    while start <= end:
        mid = start + ((end - start) // 2)

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


if __name__ == "__main__":
    inputs = [
        {"nums": [1, 6, 8, 10], "target": 1},
        {"nums": [11, 22, 33, 44, 55, 66, 77], "target": 33},
        {
            "nums": [
                -237,
                -235,
                -234,
                -226,
                -209,
                -177,
                -165,
                -150,
                -131,
                -125,
                -121,
                -101,
                -93,
                -91,
                -85,
                -23,
                -12,
            ],
            "target": 3193,
        },
    ]

    for input in inputs:
        nums, target = input.values()
        output = binary_search(nums, target)
        print(f"{nums=}, {target=}, {output=}")
        print()
