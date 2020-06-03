# 순수 노가다
def solution(s):
    tmp = 0
    for i in s:
        if i == 'p' or i == 'P':
            tmp += 1
        elif i == 'y'  or i == 'Y':
            tmp -= 1
            
    if tmp == 0:
        return True
    else:
        return False

# 문자열 내장 기능 사용
def solution(s):
    return s.lower().count('p') == s.lower().count('y')        