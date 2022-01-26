def solution(arr):
    pointer = 0
    new_arr = []
    while pointer < len(arr) - 1:
        if arr[pointer] == arr[pointer + 1]:
            pointer += 1
        else:
            new_arr.append(arr[pointer])
            pointer += 1
    new_arr.append(arr[-1])

    return new_arr