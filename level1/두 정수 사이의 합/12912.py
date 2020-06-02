# 내장 함수를 사용하지 않았을 경우
def solution(a, b):
    answer = 0
    if a < b:
        answer = (a+b)*(b-a+1) / 2
    else:
        answer = (a+b)*(a-b+1) / 2
        
    return answer


# 내장 함수를 사용할 경우 -> 속도가 특정한 케이스일 경우 더 빠름?
def solution(a, b):      
    return (abs(a-b)+1)*(a+b)//2    