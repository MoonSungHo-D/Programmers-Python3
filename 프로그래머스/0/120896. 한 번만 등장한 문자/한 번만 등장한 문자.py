from collections import Counter
def solution(s):
    answer = ''
    s_dict = Counter(s)
    for i in s_dict.items():
        
        if i[1] == 1:
            answer += i[0]
    return ''.join(sorted(answer))
