import math
def solution(brown, yellow):
    answer = []
    for i in range(1, math.ceil(math.sqrt(yellow))+1):
        if yellow % i == 0:
            y_x, y_y = yellow // i, i
            if (y_x+y_y) * 2 + 4 == brown:
                answer.append(y_x+2)
                answer.append(y_y+2)
                return answer

    return answer