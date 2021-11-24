# I, V, X, L, C, D and M.


def romanToInt(s: str) -> int:
    dictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    li = []
    i = 0
    for x in s:
        prev = dictionary[x]
        after = 0
        try:
            after = dictionary[s[i + 1]]
        except IndexError:
            print('index e')

        if prev < after:
            prev = -prev
        li.append(prev)
        i += 1
    return sum(li)
