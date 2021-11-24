from typing import List


def remove_duplicates(nums: List[int], val: int) -> int:
    while val in nums:
        nums.remove(val)
    return len(nums)


print(remove_duplicates([1,1,2,3,4,4,4,4], 1))