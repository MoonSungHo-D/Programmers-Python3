def solution(myString, pat):
    answer = ''
    myString = myString[::-1]
    pat = pat[::-1]
    count = 0
    for i, s in enumerate(myString):
        answer = myString[count:]
        if myString[i: len(pat) +i] == pat:
            
            break
        else: count +=1
    return answer[::-1]