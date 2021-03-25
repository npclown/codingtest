def solution(n):
    answer = ''
    quotient = n
    while (quotient != 0):
        remainder = quotient % 3
        quotient = quotient // 3

        if remainder == 0:
            quotient -= 1
            answer = '4' + answer
        else:
            answer = str(remainder) + answer
            
    return answer