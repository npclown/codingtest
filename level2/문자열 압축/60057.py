def solution(s):
    unit = 1
    length = len(s)
    answer = length
    while(unit != length):
        result = ''
        count = 1
        sample = ''
        for i in range(0, length, unit):
            tmp = s[i:i+unit]
            if sample == tmp:
                count += 1
            else:
                if count == 1:
                    result += sample
                else:
                    result += str(count) + sample                
                sample = tmp
                count = 1
        if count == 1:
            result += sample
        else:
            result += str(count) + sample                
                    
        answer = min(answer, len(result))
        unit += 1
    return answer