def solution(arr):
    if len(arr) == 1:
        return -1
    small = int
    for i in range(len(arr)):
        if i == 0:
            small = arr[i]
        elif arr[i] < small:
            small = arr[i]
    arr.remove(small)
    return arr