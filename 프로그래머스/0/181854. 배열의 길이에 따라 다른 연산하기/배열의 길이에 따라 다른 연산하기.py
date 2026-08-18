def solution(arr, n):
    for i, x in enumerate(arr):
        if len(arr) %2 != 0:    # 길이가 홀수
            if i % 2 ==0:       # 짝수 인덱스
                arr[i] = x+n
        else:                   # 길이가 짝수
            if i % 2 !=0:
                arr[i] = x+n
    return arr