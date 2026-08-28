def solution(arr):
    answer = []
    n = 0
    i = 0
    while len(arr) > i:
        i = 2 ** (n)
        n += 1
    
    while len(arr) < i:
        arr.append(0)
    return arr