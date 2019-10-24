#!/bin/python
# Sliding window

def findsubstrlen(s):
    candidate   = str()
    store       = {}
    result      = str()

    for n in range(len(s)):
        if s[n] in candidate:
            candidate = s[int(store[s[n]] + 1):n]
        store[s[n]] = n
        candidate += s[n]
        if len(candidate) > len(result):
            result = candidate

    return len(result)

inputstr = "nfpdmpi"
print(findsubstrlen(inputstr))