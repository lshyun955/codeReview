def solution(board, moves):
    answer = 0
    list_1 = []
    # 4 3 1 1 3 2 4
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i] - 1] != 0:
                list_1.append(board[j][moves[i] - 1])
                board[j][moves[i] - 1] = 0
                if list_1[-1:] == list_1[-2:-1]:
#                     print(list_1[-1:])
#                     print(list_1[-2:-1])
                    del list_1[-2:-1]
                    del list_1[-1:]
                    answer += 2
                    
                break
#     print(list_1)
    return answer