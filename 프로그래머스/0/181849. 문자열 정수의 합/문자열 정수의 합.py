def solution(num_str):
    answer = list(map(lambda x: int(x), [num for num in num_str]))
    return sum(answer)