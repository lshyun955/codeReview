import collections
def solution(progresses, speeds):
    proQueue = collections.deque(progresses)
    speedQueue = collections.deque(speeds)
    answer = []
    cnt = 0
    while proQueue:
        if proQueue[0] >= 100:
            proQueue.popleft()
            speedQueue.popleft()
            print("proQueue", proQueue)
            print("speedQueue", speedQueue)
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                print(answer)
            for i in range(len(proQueue)):
                proQueue[i] += speedQueue[i]
            cnt = 0
            
    if cnt > 0:
        answer.append(cnt)
    

    return answer
