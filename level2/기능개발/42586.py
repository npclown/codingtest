from collections import deque
import math

def solution(progresses, speeds):
    progress = deque(progresses)
    speed = deque(speeds)
    answer = []
    day = 0
    index = -1
    while(len(progress) != 0):
        tmp = progress.popleft()
        sp = speed.popleft()
        
        if (tmp+sp*day >= 100):
            answer[index] += 1
        else:
            day += math.ceil((100-tmp-sp*day) / sp)
            answer.append(1)
            index += 1
            
    return answer