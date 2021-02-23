board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

answer = 0

room = 0
    
result=[]
    
for i in range(len(moves)):
    room = moves[i]
        
    for j in range(len(board)):
        if board[j][room-1] >= 1:
            result.append(board[j][room-1])

            if len(result) >= 2:            
                if result[-1] == result[-2]:
                    answer += 2                    
                    del result[-1]
                    del result[-1]                   

            board[j][room-1] = 0
            break

print(result)
print(answer)