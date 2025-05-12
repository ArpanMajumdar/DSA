from bad_version import BadVersion


class Solution(BadVersion):
    def __init__(self, v):
        super().__init__(v)

    def first_bad_version(self, n):
        first, last = 1, n

        while first <= last:
            mid = first + (last - first) // 2

            if is_bad_version(mid):
                last = mid - 1
            else:
                first = mid + 1
        return first
