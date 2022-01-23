def solution(arr, divisor):
    answer = []
    for idx in range(len(arr)):
#         print(idx)
        if arr[idx] % divisor == 0:
            answer.append(arr[idx])
            print(arr[idx])
    if not answer:
        answer.append(-1)
    answer.sort()
    return answer