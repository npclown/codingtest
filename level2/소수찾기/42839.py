from itertools import permutations

def solution(numbers):
    answer = 0
    val  = []
    
    for i in range(1, len(numbers)+1):
        val += list(map(lambda x: int("".join(x)), list(permutations(numbers,i))))

    for i in list(set(val)):
        if i > 1:
            tmp = 2
            count = True
            while(tmp * tmp <= i):
                if i % tmp == 0:
                    count = False
                    break
                tmp += 1

            if count:
                answer += 1

    return answer