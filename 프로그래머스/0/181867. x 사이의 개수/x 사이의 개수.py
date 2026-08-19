def solution(myString):
    answer=[]
    myString = myString.split('x')
    for s in myString:
        answer.append(len(s))
    return answer