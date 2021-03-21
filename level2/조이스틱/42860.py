# 두번째 생각
def solution(name):
    answer = 0
    
    # 위아래 조이스틱 최소값
    for i in range(0, len(name)):
        ascii_val = ord(name[i])
        
        if ascii_val > 78:
            answer += 91 - ascii_val
        else:
            answer +=  ascii_val - 65
            
    # 좌우 조이스틱 최솟값  
    # 오른쪽으로 쭉 가는 경우와 왼쪽으로 쭉 가는 경우의 횟수는 동일 : n - 1
    # 오른쪽으로 가다가 왼쪽으로 가는 경우 : 2*L + R
    # 오른쪽으로 이동하다가 "A"를 만나면 연속된 "A"가 끝나는 지점까지 반대쪽에서 이동한다.
    # 처음부터 끝까지 길이를 모두 반복해 가장 작은 길이를 발견한다.

    n = len(name)
    one_way = n-1
    
    for index in range(n):
        next_index = index + 1
        
        while next_index < n and name[next_index] == 'A':
            next_index += 1
        
        one_way = min(one_way, 2*index + n - next_index)
    
    answer += one_way
    
    return answer

# 제일 처음 생각
def solution(name):
    r_answer = 0
    l_answer = 0
    
    tmp = ['A']*len(name)
    
    for i in range(0, len(name)):
        ascii_val = ord(name[i])
        
        if ascii_val > 78:
            r_answer += 91 - ascii_val
        else:
            r_answer +=  ascii_val - 65
            
        tmp[i] = name[i]
        
        if "".join(tmp) == name:
            break
            
        r_answer += 1
    
    tmp = ['A']*len(name)     
    
    for i in range(0, -len(name), -1):
        ascii_val = ord(name[i])
        
        if ascii_val > 78:
            l_answer += 91 - ascii_val
        else:
            l_answer += ascii_val - 65
            
        tmp[i] = name[i]
     
        if "".join(tmp) == name:
            break
        l_answer += 1
    
    return min(r_answer, l_answer)