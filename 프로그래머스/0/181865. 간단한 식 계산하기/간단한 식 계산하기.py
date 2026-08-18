def solution(binomial):
    binomial = binomial.split()
    
    binomial[0], binomial[2] = int(binomial[0]) , int(binomial[2])
    
    if binomial[1] == '+':
        answer = binomial[0] + binomial[2]
    elif binomial[1] == '-':
        answer = binomial[0] - binomial[2]
    elif binomial[1] == '*':
        answer = binomial[0] * binomial[2]
    return answer