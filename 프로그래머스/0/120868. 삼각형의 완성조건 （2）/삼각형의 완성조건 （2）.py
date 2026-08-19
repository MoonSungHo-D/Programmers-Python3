def solution(sides):
    a, b = max(sides), min(sides)
    count=0
    for i in range(1, a+b):
        if i + b> a:
            count +=1
    return count