def solution(s):
    answer = int(s)
    return answer

#내장함수 사용하지 않기
def strToInt(str):
    result = 0
    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)
    return result