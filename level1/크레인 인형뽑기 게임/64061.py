def solution(board, moves):
    answer = 0
    length = len(board)
    top = [0 for i in range(length)]

    for index in range(length):
        for i, num in enumerate(board[index]):
            if num == 0:
                top[i] += 1

    basket = []
    for move in moves:
        location = top[move - 1]

        if location < length and board[location][move - 1] != 0:
            basket.append(board[location][move - 1])
            board[location][move - 1] = 0
            top[move - 1] += 1

            if len(basket) > 1 and basket[len(basket) - 1] == basket[len(basket) - 2]:
                basket.pop()
                basket.pop()
                answer += 2

    return answer