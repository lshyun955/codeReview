def solution(array, commands):
    answer = []
    
    for com in commands:
        i,j,k = com[0], com[1], com[2]
        num = sorted(array[i-1:j])
        answer.append(num[k-1])
    return answer