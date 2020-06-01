def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        test = sorted(array[commands[i][0]-1:commands[i][1]])
        answer.append(test[commands[i][2]-1])    
    return answer