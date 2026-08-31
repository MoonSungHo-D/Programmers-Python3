def solution(order):
    n_list = [i for i in str(order)]
    count = 0
    for i in n_list:
        if (i == '3') | (i == '6') | (i == '9'):
            count += 1
    return count