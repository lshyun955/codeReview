def solution(a, b):
    sum = 0
    for i in range(len(a)):
        output = a[i] * b[i]
        sum += output

    return sum