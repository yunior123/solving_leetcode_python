def reverse(x: int) -> int:
    s = str(x)
    i = len(s)-1
    rev = ''
    for _ in s:
        if s[i] == "-":
            rev = "-" + rev
            break

        rev += s[i]
        i -= 1
    # -231 <= x <= 231 - 1
    if pow(-2, 31) <= int(rev) and int(rev) <= pow(2, 31):
        return int(rev)
    return 0


print(reverse(1534236469))
