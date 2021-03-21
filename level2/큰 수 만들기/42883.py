def solution(number, k):
    answer = ''
    start = 0
    
    for end in range(k, len(number)):
        tmp_list = number[start:end+1]
        if len(tmp_list) == 1:
            answer += "".join(number[start:])
            break
        else:
            tmp_max = '0'
            tmp_index = 0
            for i in range(len(tmp_list)):
                if tmp_list[i] > tmp_max:
                    tmp_max = tmp_list[i]
                    tmp_index = i
                    if tmp_list[i] == '9':
                        break
            answer += tmp_max
            start += tmp_index +1        
        
    return answer

## 1o번 테스트 케이스 시간 초과건
def solution(number, k):
    answer = ''
    start = 0
    number_list = list(number)

    for end in range(k, len(number)):
        tmp_list = number_list[start:end+1]
        a = max(tmp_list)
        answer += a
        start += tmp_list.index(a) +1        
        
    return answer