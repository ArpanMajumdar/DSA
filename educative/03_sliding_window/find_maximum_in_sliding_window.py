from collections import deque

# Solution
# 1. First, we check if the input list contains only one element. If it does, we directly return the input list because there is only one maximum element.
# 2. Then, we process the first w elements of the input list. We will use a deque to store the indexes of the candidate maximums of each window.
# 3. For each element, we perform the clean-up step, removing the indexes of the elements from the deque whose values are smaller than or equal to the value of the element we are about to add to the deque. Then, we append the index of the new element to the back of the deque.
# 4. After the first w elements have been processed, we append the element whose index is present at the front of the deque to the output list as it is the maximum in the first window.
# 5. After finding the maximum in the first window, we iterate over the remaining input list. For each element, we repeat Step 3 as we did for the first w elements.
# 6. Additionally, in each iteration, before appending the index of the current element to the deque, we check if the first index in the deque has fallen out of the current window. If so, we remove it from the deque.
# 7. Finally, we return the list containing the maximum elements of each window.


def find_max_sliding_window(nums: list[int], w: int) -> list[int]:
    n = len(nums)
    current_window = deque(maxlen=n)
    output = []

    # Optimization for nums with single element
    if n == 1:
        return nums

    # Iterate over first w elements
    for i in range(w):
        cleanup(nums, current_window, i)
        current_window.append(i)

    output.append(nums[current_window[0]])

    for i in range(w, n):
        cleanup(nums, current_window, i)
        current_window.append(i)
        if current_window[0] < i - w + 1:
            current_window.popleft()
        output.append(nums[current_window[0]])

    # print(f"current_window = {current_window}")
    # print(f"output = {output}")
    return output


def cleanup(nums: list[int], current_window: deque, current_num_idx: int):
    while current_window and nums[current_num_idx] >= nums[current_window[-1]]:
        current_window.pop()


if __name__ == "__main__":
    inputs = [([2, 4, 3, 6, 5, 4, 1, 10], 3)]

    for nums, w in inputs:
        output = find_max_sliding_window(nums, w)
        print(f"nums = {nums}, w = {w}")
        print(f"output = {output}")
        print()
