from collections import deque
import numpy as np

def solution(bridge_length, weight, truck_weights):
    bridge = deque(np.zeros(bridge_length))
    answer = 0
    bridge_weight = 0
    
    while (len(truck_weights) != 0 or bridge_weight != 0):
        bridge_weight -= bridge[0]
        bridge.popleft()
        if len(truck_weights) == 0:
            bridge.append(0)
        else:
            if(bridge_weight + truck_weights[0] > weight):
                bridge.append(0)
            else:
                bridge_weight += truck_weights[0]
                bridge.append(truck_weights.pop(0))
                              
        answer += 1
       
    return answer