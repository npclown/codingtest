def solution(n, lost, reserve):
    answer = 0
    student = [1 for i in range(n)]
    
    for i in lost:
        student[i-1] -= 1
        
    for i in reserve:
        student[i-1] += 1        
    
    for i, cnt in enumerate(student):
        if cnt >= 1:
            answer += 1
        elif cnt  == 0:
            if i-1>=0 and student[i-1] == 2:
                answer += 1 
                student[i-1] -=  1
                student[i] += 1
            elif i+1 < len(student) and student[i+1] == 2:
                answer += 1 
                student[i+1] -=  1
                student[i] += 1
                
    return answer