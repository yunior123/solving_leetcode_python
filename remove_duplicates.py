from typing import List


def remove_duplicates(nums: List[int]) -> int:
    dct = {}
    i = len(nums)
    if i == 0:
        return 0
    while i > 0:
        if nums[i - 1] in dct:
            nums.remove(nums[i - 1])
            i -= 1
            continue
        dct[nums[i - 1]] = ""
        i -= 1
    return len(nums)


print(remove_duplicates([1,1,2,3,4,4,4,4]))