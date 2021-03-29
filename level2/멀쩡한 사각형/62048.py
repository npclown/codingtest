import math

# def solution(w,h):
#     return w*h - (w+h-math.gcd(w,h))

def solution(w,h):
    answer = 0
    
    tmp_w = min(w,h)
    tmp_h = max(w,h)
    
    if w == h:
        return w*h - w
    elif w == 1 or h == 1:
        return 0
    else:
        for x in range(1,w):
            answer += h - math.ceil(h/w* x)
    return answer * 2