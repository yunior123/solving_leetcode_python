# Given
# two
# integers
# n and k,
# return all
# possible
# combinations
# of
# k
# numbers
# out
# of
# the
# range[1, n].
#
# You
# may
# return the
# answer in any
# order.
#
# Example
# 1:
#
# Input: n = 4, k = 2
# Output:
# [
#     [2, 4],
#     [3, 4],
#     [2, 3],
#     [1, 2],
#     [1, 3],
#     [1, 4],
# ]

def combine(n, k):

    result = []

    def combine_fn(numbers, index):
        if len(numbers) == k:
            result.append(numbers.copy())
            return

        for i in range(index, n + 1):
            numbers.append(i)
            combine_fn(numbers, i + 1)
            numbers.pop()
    combine_fn([], 1)
    return result





print(combine(4,2))