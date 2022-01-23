def solution(s):
    answer = ''
    ssplit = list(s)
#     print(ssplit)
    lenssplit = len(ssplit)
    if lenssplit % 2 == 0:
        answer += ssplit[lenssplit // 2 - 1]
        answer += ssplit[lenssplit // 2]
    
    else:
        answer += ssplit[lenssplit // 2]
    return answer