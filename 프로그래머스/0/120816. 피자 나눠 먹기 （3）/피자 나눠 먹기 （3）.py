def solution(slice, n):
    answer = int(n// slice) + 1
    return answer if n%slice !=0 else n//slice 