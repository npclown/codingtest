from collections import deque

def solution(prices):
    answer = [0] * len(prices)

    queue = deque(prices)
    index = 0
    
    while(len(queue)!=0):
        tmp = queue.popleft()
        for price in queue:
            answer[index] += 1
            if tmp > price:
                break
        index+=1
    return answer