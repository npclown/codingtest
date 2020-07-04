def solution(s):
    answer = []
    for word in s.split(' '):
        tmp = ''
        for i in range(len(word)):
            if i % 2 == 0:
                tmp += word[i].upper()
            else:
                tmp += word[i].lower()
        answer.append(tmp)

    return " ".join(answer)

# 미리 s.strip()을 통해 앞뒤 공백을 없애 주는 경우는 특정 테스트 케이스일 경우 오류가 발생한다.
# 문제가 요구하는 정확한 상황에 대해서 판단이 어려운 문제인거 같다.

