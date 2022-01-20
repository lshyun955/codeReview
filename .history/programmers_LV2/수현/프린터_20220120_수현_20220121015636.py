import collections
# locations은 index..!
def solution(priorities, location):
    answer = 0
    priorities = collections.deque(priorities)
    tempQueue = collections.deque([num for num in range(len(priorities))])
    tempVal = priorities.popleft()
    while priorities:
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
        tempVal = priorities.popleft()
    return answer + 1