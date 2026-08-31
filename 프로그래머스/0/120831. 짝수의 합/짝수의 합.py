def solution(n):
    lst = []
    for i in range(1,n+1):
        
        if i %2 == 0:
            lst.append(i)
    return sum(lst)