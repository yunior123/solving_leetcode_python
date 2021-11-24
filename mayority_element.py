from typing import List


def majorityElement(nums: List[int]) -> int:
	candidate = nums[0]
	count = 1

	for i in range(1, len(nums)):
		if not count:
			candidate = nums[i]

		if nums[i] == candidate:
			count += 1

		else:
			count -= 1

	return candidate

print(majorityElement([1,2,2,1,3,1,5]))