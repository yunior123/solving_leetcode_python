def permute(nums):
    # DPS with swapping
    res = []
    if len(nums) == 0:
        return res
    get_permute(res, nums, 0)
    return res


def get_permute( res, nums, index):
    if index == len(nums):
        res.append(list(nums))
        return
    for i in range(index, len(nums)):
        nums[i], nums[index] = nums[index], nums[i]
        # s(n) = 1 + s(n-1)
        get_permute(res, nums, index + 1)
        nums[i], nums[index] = nums[index], nums[i]


print(permute([1,2,3]))