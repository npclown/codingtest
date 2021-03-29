def solution(numbers, target):
    final = [0]
    
    for i in numbers:
        tmp = []
        
        for j in final:
            tmp.append(j+i)
            tmp.append(j-i)
        final = tmp
    
    return final.count(target)