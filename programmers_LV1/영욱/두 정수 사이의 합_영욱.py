def solution(a, b):
    if a == b:
        return a
    if a < b:
        sum = 0
        for i in range(a, b + 1):
            sum += i
        return sum
    if a > b:
        sum = 0
        for i in range(b, a + 1):
            sum += i
        return sum
