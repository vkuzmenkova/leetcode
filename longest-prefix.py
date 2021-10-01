from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    temp = sorted(strs, key=len)
    prefix = ''

    for i in range(len(temp[0])):
        is_the_same = True
        for string in strs:
            if string[i] != temp[0][i]:
                is_the_same = False
                break
        if is_the_same:
            prefix += temp[0][i]
        else:
            break

    return prefix


strs = ["cir","car"]
print(longestCommonPrefix(strs))
