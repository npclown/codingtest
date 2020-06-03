def solution(s):
    length = len(s)

    return s.isdigit() and (length == 4 or length == 6):
    