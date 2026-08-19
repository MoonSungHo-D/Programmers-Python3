def solution(number):
    
    answer = []
    
    for i in range(len(number)):
        answer.append(int(number[i]))
    
    return sum(answer) % 9