def solution(my_string, is_prefix):
    lst = []
    
    for i in range(len(my_string)):
        lst.append(my_string[:i+1])
    if is_prefix in lst:
        return 1
    else:
        return 0