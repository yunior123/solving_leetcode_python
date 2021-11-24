def longestCommonPrefix(strs: list[str]) -> str:
    if len(strs) == 0:
        return ""
    i = 0
    s = ""
    for x in strs[0]:
        bool_li = []
        for c in strs:
            try:
                if x == c[i]:
                    bool_li.append(True)
                else:
                    bool_li.append(False)
            except IndexError:
                bool_li.append(False)

        if all(bool_li):
            s += x
        else:
            break

        i += 1

    return s
