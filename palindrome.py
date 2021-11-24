# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#best solution
class Solution:
    # @param x, an integer
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False

        ranger = 1
        while x / ranger >= 10:
            ranger *= 10

        while x:
            left = x / ranger
            right = x % 10
            if left != right:
                return False

            x = (x % ranger) / 10
            ranger /= 100

        return True

# my solution
def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    li = []
    while True:
        remainder = x % 10
        li.append(remainder)
        x = x // 10
        if x < 1:
            break

    rev = reverse_list(li)
    if li == rev:
        return True
    return False


def reverse_list(li: list[int]) -> list[int]:
    i = len(li)
    new_list = []
    for _ in range(len(li)):
        i -= 1
        new_list.append(li[i])

    return new_list