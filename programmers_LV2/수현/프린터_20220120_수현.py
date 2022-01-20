import collections
# locations은 index..!
def solution(priorities, location):
    answer = 0
    priorities = collections.deque(priorities)
    # index 담을 큐 생성
    tempQueue = collections.deque([num for num in range(len(priorities))])
    while priorities:
        tempVal = priorities.popleft()
        if priorities:
            print('tempVal :::::',tempVal)
            print('temp :::::',tempQueue)
            print('prior :::::',priorities)
            if tempVal < max(priorities):
                tempQueue.append(tempQueue.popleft())
                priorities.append(tempVal)
            else:
                answer += 1
                if tempQueue[0] == location:
                    return answer
                else:
                    tempQueue.popleft()
        print(answer)
    return answer + 1