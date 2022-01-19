def solution(n):
    a = list(str(n))
    for i in range(len(a)):
        a[i] = int(a[i])
    return sum(a)