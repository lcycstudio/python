"""
Convert One String to Another with minimum operation in Python
stopping criterion: index1=len(s1), index2=len(s2)
3 action functions: deleteOp, insertOp, replaceOp
"""


def findMinOperation(s1, s2, index1, index2):
    if index1 == len(s1):
        return len(s2) - index2
    if index2 == len(s2):
        return len(s1) - index1
    if s1[index1] == s2[index2]:
        return findMinOperation(s1, s2, index1 + 1, index2 + 1)
    else:
        deleteOp = 1 + findMinOperation(s1, s2, index1, index2 + 1)
        insertOp = 1 + findMinOperation(s1, s2, index1 + 1, index2)
        replaceOp = 1 + findMinOperation(s1, s2, index1 + 1, index2 + 1)
        return min(deleteOp, insertOp, replaceOp)


print(findMinOperation("table", "tbrlt", 0, 0))
print(findMinOperation("table", "tbrltt", 0, 0))
print(findMinOperation("catch", "carch", 0, 0))
