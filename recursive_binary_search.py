from typing import List


def find_peak_value(numbers: List[int], first: int, last: int, length: int) -> int:
    midpoint = (first + last) // 2
    if (midpoint == 0 or numbers[midpoint] > numbers[midpoint - 1]) and (
            midpoint == length - 1 or numbers[midpoint] > numbers[midpoint + 1]):
        return midpoint
    # this means that there has to be a peak value to the left
    elif midpoint > 0 and numbers[midpoint - 1] > numbers[midpoint]:
        return find_peak_value(numbers, first, midpoint - 1, length)
    else:
        return find_peak_value(numbers, midpoint + 1, last, length)


arr = [3, 4, 2, 6, 7, 8, 9]
n = len(arr)
print(find_peak_value(arr, 0, len(arr) - 1, n))
