from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    first = 0
    last = len(numbers) - 1

    while first < last:
        sum_two = numbers[first] + numbers[last]
        if sum_two == target:
            return [first + 1, last + 1]
        elif sum_two < target:
            first += 1
        else:
            last -= 1



