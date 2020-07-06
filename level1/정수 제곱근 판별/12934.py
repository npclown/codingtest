import math

def solution(n):
    answer = 0
    tmp = round(math.sqrt(n))
    if tmp * tmp == n:
        answer = (tmp+1)*(tmp+1)
    else:
        answer = -1
    return answer


def solution(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return -1