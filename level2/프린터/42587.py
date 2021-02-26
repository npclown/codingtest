from collections import deque

# 코드는 이게 더 깔끔함
def solution(priorities, location):
    queue = deque([(x,i) for i,x in enumerate(priorities)])
    max_value = max(queue)[0]
    answer = 0
    while(True):
        tmp = queue.popleft()
        answer+=1

        if len(queue) == 0:
            break
        else:        
            if tmp[0] == max_value:
                max_value = max(queue)[0]
                if tmp[1] == location:
                    break
            else:
                queue.append(tmp)
                answer-=1
                
        
    return answer

# 속도는 이게 더 빠름
def solution(priorities, location):
    queue = deque(priorities)
    check = deque([0]*len(priorities))
    check[location] = 1
    max_value = max(queue)
    count = 0
    while(True):
        tmp = queue.popleft()
        chk = check.popleft()
        count+=1

        if len(queue) == 0:
            break
        else:        
            if tmp ==  max_value:
                max_value = max(queue)
                if chk == 1:
                    break
            else:
                queue.append(tmp)
                check.append(chk)
                count-=1
        
    return count