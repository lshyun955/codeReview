def solution(num):
    count = 0
    answer = num

    if num == 1:
        return count
    while count <= 500:
        if answer % 2 == 0:
            answer = answer / 2
        elif answer % 2 == 1:
            answer = answer * 3 + 1
        count = count + 1

        if answer == 1:
            return count

    return -1