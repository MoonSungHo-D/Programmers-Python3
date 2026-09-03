def solution(n):
    n_list= []
    n = str(n)
    result = 0
    for i in n:
        n_list.append(i)
        
    for i in range(len(n_list)):
        result += int(n_list[i])
    return result