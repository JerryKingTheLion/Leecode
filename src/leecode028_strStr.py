def getNext(s:str)->int:
    j = 0
    str = list(s)
    next = [0 for i in range(len(s))]

    for i in range(1, len(s)):
        while (j > 0 and s[i] != s[j]):
            j = next[j - 1]

        if s[i] == s[j] :
            j += 1

        next[i] = j

    return next


def strStr(haystack: str, needle: str) -> int:
    a = len(needle)
    b = len(haystack)
    if a == 0:
        return 0
    next = getNext(needle)
    p = -1
    for j in range(b):
        while p >= 0 and needle[p + 1] != haystack[j]:
            p = next[p-1]
        if needle[p + 1] == haystack[j]:
            p += 1
        if p == a - 1:
            return j - a + 1
    return -1