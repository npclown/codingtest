def solution(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


def solution(num):
    return ["Even", "Odd"][num & 1]

def solution(num):
    return "Even" if num%2 == 0 else "Odd"