def solution(answers):
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = []
    length = len(answers)

    tmp = {1: 0, 2: 0, 3: 0}
    for i in range(length):
        if person1[i % 5] == answers[i]:
            tmp[1] += 1

    for i in range(length):
        if person2[i % 8] == answers[i]:
            tmp[2] += 1

    for i in range(length):
        if person3[i % 10] == answers[i]:
            tmp[3] += 1

    max_value = max(tmp.values())

    for key, value in tmp.items():
        if value == max_value:
            answer.append(key)

    return answer