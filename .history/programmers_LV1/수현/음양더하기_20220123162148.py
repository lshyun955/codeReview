def solution(absolutes, signs):
    realNumList = []
    for idx in range(len(absolutes)):
        if not signs[idx]:
            realNumList.append(-absolutes[idx])
        else:
            realNumList.append(absolutes[idx])
    answer = sum(realNumList)
    return answer