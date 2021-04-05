def solution(numbers, hand):
    answer = ''
    r_position = (3,2)
    l_position = (3,0)
    position = {1 : (0,0), 2 : (0,1), 3 : (0,2), 4: (1,0), 5:(1,1), 6: (1,2), 7:(2,0), 8:(2,1), 9:(2,2), 0:(3,1)}
    line = { 1: 'L', 4: 'L', 7: 'L', 2: 'M', 5: 'M', 8: 'M', 0: 'M', 3: 'R', 6 : 'R', 9 : 'R'}
    
    for i in numbers:
        location = line[i]
        if location == 'M':
            l_distance = abs(position[i][0]-l_position[0])+abs(position[i][1]-l_position[1])
            r_distance = abs(position[i][0]-r_position[0])+abs(position[i][1]-r_position[1])

            if l_distance < r_distance:
                answer += 'L'
                l_position = position[i]
            elif l_distance > r_distance:
                answer += 'R'
                r_position = position[i]    
            else:
                if hand == 'right':
                    answer += 'R'
                    r_position = position[i]    
                else:
                    answer += 'L'
                    l_position = position[i]
        elif location == 'L':
            answer += 'L'
            l_position = position[i]
        elif location == 'R':
            answer += 'R'
            r_position = position[i]
    return answer