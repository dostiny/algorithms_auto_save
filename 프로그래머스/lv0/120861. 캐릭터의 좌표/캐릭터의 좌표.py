def solution(keyinput, board):
    answer = [0, 0]
    max_x, max_y = board[0] // 2, board[1] // 2
    for i in keyinput:
        if i == 'up' and answer[1] < max_y:
            answer[1] += 1
        elif i == 'right' and answer[0] < max_x:
            answer[0] += 1
        elif i == 'down' and answer[1] > -max_y:
            answer[1] -= 1
        elif i == 'left' and answer[0] > -max_x:
            answer[0] -= 1
    return answer