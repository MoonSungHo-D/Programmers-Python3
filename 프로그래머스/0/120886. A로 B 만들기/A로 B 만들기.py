def solution(before, after):
    answer= 1
    before = list(before)
    after = list(after)
    for i, s in enumerate(before):
        if s in after:
            after.remove(s)
        else:
            answer=0
        
        
    return answer