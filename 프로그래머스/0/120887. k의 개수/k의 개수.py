def solution(i, j, k):
    count = 0
    for n in range(i, j+1):
        n = str(n)
        count += n.count(str(k))
        
    return count