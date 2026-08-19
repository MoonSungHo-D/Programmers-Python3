def solution(num_list):
    hol = 0
    zak = 0
    for i, n in enumerate(num_list):
        if i % 2 != 0:
            zak += n
            
        else:
            hol += n
    answer = [hol, zak]  
    return max(answer)