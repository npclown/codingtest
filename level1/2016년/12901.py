def solution(a, b):
    date = [0, 31, 60, 91, 121,152,182,213,244,274,305,335]
    day = {1:"FRI", 2 : "SAT" , 3: "SUN", 4:"MON", 5:"TUE", 6:"WED", 0:"THU"}
    
    tmp = date[a-1] + b
    
    answer = day[tmp%7]
    return answer