def solution(my_string, letter):
    lst = []
    for i in my_string:
        if i != letter:
            lst.append(i)
    
    return "".join(lst)