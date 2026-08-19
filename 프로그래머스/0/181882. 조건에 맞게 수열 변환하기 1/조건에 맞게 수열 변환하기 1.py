def solution(arr):
    for i, n in enumerate(arr):
        if n >=50 and n % 2 ==0 :
            arr[i] = int(n / 2)
        elif n < 50 and n%2 != 0:
            arr[i] = int(n*2)
    return arr