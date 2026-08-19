def solution(todo_list, finished):
    answer = []
    finished = [int(i) for i in finished]
    for i in range(len(finished)):
        if finished[i] == 0:
            answer.append(todo_list[i])
    return answer