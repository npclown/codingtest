# 단순한 단복문
def solution(seoul):
    answer = ''
    for i, arr in enumerate(seoul):
        if arr == "Kim":
            answer = "김서방은 {}에 있다".format(i)
            return answer


# 숏코딩
def solution(seoul):
    return "김서방은 {}에 있다".format(seoul.index("Kim"))