def solution(n):
    answer=set()
    for i in range(1,n+1):
        count=0
        for j in range(1, i+1):
            if i % j ==0:
                count +=1
            
                if count >=3:
                    answer.add(i)
   
    return len(answer)  