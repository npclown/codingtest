#일반적인 풀이
def solution(strings, n):
    answer = []
    for i, txt in enumerate(strings):
        strings[i] = strings[i][n] + txt
    
    strings.sort()
    
    for txt in strings:
        answer.append(txt[1:])
        
    return answer

#lambda 방식
def solution(strings, n):
    return sorted(strings, key=lambda str: (str[n], str))     