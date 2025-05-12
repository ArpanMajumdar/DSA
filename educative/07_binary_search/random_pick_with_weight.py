import random


class RandomPickWithWeight:
    def __init__(self, weights):
        # Write your code here
        # The weights array, consisting of integers, is passed to the constructor
        self.weights = weights
        self.cumsum = []
        curr_sum = 0
        for weight in self.weights:
            curr_sum += weight
            self.cumsum.append(curr_sum)

    def pick_index(self):
        total_sum = self.cumsum[-1]
        key = random.randint(1, total_sum)
        start, end = 0, len(self.cumsum)

        print(f"cumsum={self.cumsum}")
        while start < end:
            mid = start + (end - start) // 2
            print(f"{key=}, {start=}, {end=}, {mid=}")

            if key > self.cumsum[mid]:
                start = mid + 1
            else:
                end = mid
        return start


if __name__ == "__main__":
    weights = [5, 10, 15, 20, 25, 30]
    random_pick = RandomPickWithWeight(weights)
    print(f"{weights=}, random_index={random_pick.pick_index()}")
