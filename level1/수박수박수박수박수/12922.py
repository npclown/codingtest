#내 풀이
def solution(n):
    return '수박'*(n//2) + '수'*(n%2)

#색다른 풀이
def solution(n):
    s = "수박" * n
    return s[:n]

