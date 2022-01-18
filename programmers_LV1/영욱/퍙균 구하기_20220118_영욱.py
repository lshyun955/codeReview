def solution(arr):
    sum = 0
    for number in arr:
        sum = sum + number

    answer = sum / len(arr)
    return answer