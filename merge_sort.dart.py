from typing import List


def merge_sort(numbers: List[int]) -> List[int]:
    if len(numbers) == 1:
        return numbers
    middle = (len(numbers) // 2)
    left_part = merge_sort(numbers[:middle])
    right_part = merge_sort(numbers[middle:])

    return merge(left_part, right_part)


def merge(left_part: List[int], right_part: List[int]) -> List[int]:
    numbers = []
    i = 0
    j = 0
    while len(left_part) > i and len(right_part) > j:
        if left_part[i] < right_part[j]:
            numbers.append(left_part[i])
            i = i + 1
        else:
            numbers.append(right_part[j])
            j = j + 1

    while len(left_part) > i:
        numbers.append(left_part[i])
        i = i + 1

    while len(right_part) > j:
        numbers.append(right_part[j])
        j = j + 1

    return numbers


print(merge_sort([4,7,1,2]))