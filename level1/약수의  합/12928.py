##
def solution(n):
    answer = 0
    if n == 0:
        return 0
    elif n == 1:
        return 1

    for i in range(1, n + 1):
        if n % i == 0:
            answer += (i)

    return answer

##
def solution(n):
    answer = 0
    if n == 0:
        return answer

    for i in range(1, int(math.sqrt(n + 1)) + 1):
        if n % i == 0:
            answer += i
            if i != n // i:
                answer += n // i

    return answer

##
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])