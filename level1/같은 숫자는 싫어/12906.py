def solution(arr):
    answer = []
    tmp = -1
    for i in arr:
        if i == tmp:
            continue
        tmp = i
        answer.append(i)
    
    return answer