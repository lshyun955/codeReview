def solution(n):
    wm = {0 : '수', 1 : '박'}
    answer = ''
    for idx in range(1,n+1):
        if idx%2 == 1:
            answer += wm[0]
        else:
            answer += wm[1]
    return answer