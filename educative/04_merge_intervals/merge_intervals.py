# Problem
# We are given an array of closed intervals, intervals, where each interval has a start time and an end time. The input array is sorted with respect to the start times of each interval.
# For example, intervals = [[1,4],[3,6],[7,9]]
# Constraints
# 1 <= intervals.length <= 10^3
# intervals[i].length = 2
# 0 <= start_time <= end_time <= 10^4

# Solution
# 1. Sort the intervals array by start_time (skip if already sorted).
# 2. Insert the first interval from input list to output list.
# 3. Traverse the input intervals list
#   3.1 If the current interval is overlapping with the last interval of the output list, merge these intervals.
#   3.2 Else, add the current interval to the end the the output list

# Time complexity: O(n)

# Space complexity: O(1)


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if intervals is None or len(intervals) < 2:
        return intervals

    output = [intervals[0].copy()]

    output_idx = 0
    for i in range(1, len(intervals)):
        interval = intervals[i]
        cur_interval_start, cur_interval_end = interval[0], interval[1]
        if cur_interval_start <= output[output_idx][1]:
            output[output_idx][1] = max(output[output_idx][1], cur_interval_end)
        else:
            output.append(interval.copy())
            output_idx += 1

    return output


if __name__ == "__main__":
    inputs = [
        {"intervals": [[1, 6], [2, 4]]},
        {"intervals": [[1, 8]]},
        {"intervals": [[2, 9], [3, 5], [4, 8]]},
        {"intervals": [[2, 4], [3, 5], [4, 5], [6, 10], [12, 14]]},
        {"intervals": [[1, 5], [4, 6], [6, 8], [11, 15]]},
    ]

    for input in inputs:
        output = merge_intervals(input["intervals"])
        print(f"intervals = {input['intervals']}")
        print(f"output = {output}")
        print()
