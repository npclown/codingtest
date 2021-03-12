import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while(True):
        if scoville[0] >= K:
            return answer
        else:
            if len(scoville) < 2:
                return -1
            else:
                tmp1 = heapq.heappop(scoville)
                tmp2 = heapq.heappop(scoville)
                heapq.heappush(scoville,tmp1 + tmp2*2)
                answer += 1
    return scoville

# 단순 스택 사용
#     while(True):
#         if scoville_sort[-1] >= K:
#             return answer
#         else:
#             if len(scoville_sort) < 2:
#                 return -1
#             else:
#                 tmp1 = scoville_sort.pop()
#                 tmp2 = scoville_sort.pop()
#                 scoville_sort.append(tmp1+tmp2*2)
#                 scoville_sort.sort(reverse=True)
#                 answer += 1