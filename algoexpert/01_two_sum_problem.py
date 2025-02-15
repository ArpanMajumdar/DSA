from typing import Optional, Tuple


# Time complexity: O(n)
# Space complexity: O(n)
def two_sum_hashmap_method(
    arr: list[int], target_sum: int
) -> Optional[Tuple[int, int]]:
    arr_set = set()
    for x in arr:
        y = target_sum - x
        if (
            y in arr_set
        ):  # If the diff between target sum and curr element exists in the set, then we are done.
            return x, y
        else:  # Store the current num in set
            arr_set.add(x)
    return None


# Time complexity: O(nlog(n))
# Space complexity: O(1)
def two_sum_two_pointer_method(
    arr: list[int], target_sum: int
) -> Optional[Tuple[int, int]]:
    # Sort the array
    arr.sort()

    left = 0
    right = len(arr) - 1

    while left < right:
        curr_sum = arr[left] + arr[right]

        if curr_sum < target_sum:
            left += 1
        elif curr_sum > target_sum:
            right -= 1
        else:
            return arr[left], arr[right]

    return None


def main():
    arr = [3, 5, -4, 8, 11, 1, -1, 6]
    target_sum = 10
    nums = two_sum_two_pointer_method(arr, target_sum)

    if nums is not None:
        print(f"x={nums[0]}, y={nums[1]}")
    else:
        print(f"No two numbers have sum={target_sum}")


if __name__ == "__main__":
    main()
