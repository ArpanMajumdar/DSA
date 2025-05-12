def binary_search_rotated(nums: list[int], target: int) -> int:
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = low + ((high - low) // 2)
        print(f"{low=}, {high=}, {mid=}")
        if nums[mid] == target:
            return mid
        # Left half is sorted and target lies in left half
        elif nums[low] <= nums[mid - 1] and (nums[low] <= target <= nums[mid - 1]):
            high = mid - 1
        # Left half is sorted but target is not in left half
        elif nums[low] <= nums[mid - 1]:
            low = mid + 1
        # Right half is sorted and target lies in right half
        elif nums[mid + 1] <= nums[high] and (nums[mid + 1] <= target <= nums[high]):
            low = mid + 1
        # Right half is sorted and target is not in right half
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    inputs = [{"nums": [6, 7, 1, 2, 3, 4, 5], "target": 5}]
    for input in inputs:
        nums, target = input.values()
        output = binary_search_rotated(nums, target)
        print(f"{nums=}, {target=}, {output=}")
        print()
