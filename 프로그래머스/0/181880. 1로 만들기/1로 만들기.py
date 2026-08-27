def mul2(n):
    count = 0
    while n != 1 :
        n = n //2
        count += 1
    return count

def solution(num_list):
    count2 = 0
    for n in num_list:
        count = mul2(n)
        count2 += count
    return count2
