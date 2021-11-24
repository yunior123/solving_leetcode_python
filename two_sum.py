from typing import Any


def two_sum(self, nums: list[int], target: int) -> Any:
    prev_map = {}  # val : index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[n] = i
    return
