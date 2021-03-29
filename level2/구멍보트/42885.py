from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    dq = deque(people)
    length = len(people)
    
    while(True):
        if length == 0:
            break
        elif length == 1:
            dq.popleft()
            length -= 1
            answer += 1
            break
        else:
            tmp = dq.popleft()
            length -= 1
            
            if tmp + dq[-1] <= limit:
                dq.pop()
                length -= 1
                
            answer += 1
            
    return answer