def solution(numbers, n):
    count=0
    for i in numbers:
        count += i
        if count>n:
            break
    
    return count