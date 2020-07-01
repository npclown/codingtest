def solution(s, n):
    answer = ''
    for word in s:
        if word.isupper():
            tmp = ord(word)-65+n
            answer += chr(tmp%26 + 65)
        elif word.islower():
            tmp = ord(word)-97+n
            answer += chr(tmp%26 + 97)
        else:
            answer += word
    return answer