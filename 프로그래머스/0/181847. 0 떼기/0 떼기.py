def solution(nl):
    nl_list= []
    for i in range(len(nl)):
        nl_list.append(nl[i])
   
    for i in range(len(nl_list)):
        
        if nl_list[0] != '0':
            break
        nl_list.remove("0")
    return ''.join(nl_list)