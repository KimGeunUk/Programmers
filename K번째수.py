def solution(array, commands):

    answer = []

    a =[]    

    for i in range(len(commands)):       

        a.append(sorted(array[commands[i][0]-1:commands[i][1]]))
    
        answer.append(a[i][commands[i][2]-1])

    print(a)    
    
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3],[4, 4, 1],[1, 7, 3]]))