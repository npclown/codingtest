def solution(citations):
    citations.sort()
    h_index = 0
    index = 0
    length = len(citations)
    
    while(length > index):
        if citations[index] >= h_index and length - index >= h_index:
            h_index += 1    # 다음 h_index 증가한 경우를 테스트 하기 위해서 사용
        else:
            index += 1
        
        if length - index < h_index:
            break

    return h_index - 1 