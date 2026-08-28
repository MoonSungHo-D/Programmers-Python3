def solution(num_list, n):
    num_list.reverse()
    lister = []
    answer = []
    for i in range(len(num_list)//n):
        lister = []
        for j in range(n):
            lister.append(num_list.pop())
        answer.append(lister)
    return answer