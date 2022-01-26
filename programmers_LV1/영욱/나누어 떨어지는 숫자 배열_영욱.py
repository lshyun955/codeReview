def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])

    if not answer:
        return [-1]
    else:
        return sorted(answer)
