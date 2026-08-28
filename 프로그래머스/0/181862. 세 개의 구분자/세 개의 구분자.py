def solution(myStr):
    answer = []
    result = ''
    for s in myStr:
        if s !='a' and s !='b' and s !='c':
            result += s
        else:
            answer.append(result)
            result = ''
    if result != '':
        answer.append(result)
    
    answer = [x for x in answer if x != '']
    return answer if len(answer) != 0 else ['EMPTY']