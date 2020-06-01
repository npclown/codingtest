##처음 생각한 코드
def solution(s):
    answer = ''
    length = len(s)
    if length % 2 == 0:
        answer = s[length//2-1:length//2+1]
    else:
        answer = s[length//2]
    return answer

##좀더 간단한 코드
def solution(s):
    return s[(len(s)-1)//2:len(s)//2+1]    