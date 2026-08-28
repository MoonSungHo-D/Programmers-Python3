from collections import Counter
def solution(strArr):
    answer = 0
    lst = []
    for i in strArr:
        lst.append(len(i))
    dit = Counter(lst)
    dit.values()
    return max(dit.values())