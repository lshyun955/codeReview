def solution(s):
    if len(s) == 4 or len(s) == 6:
        pass
    else:
        return False

    lst = list(s)
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for i in range(len(lst)):
        if lst[i] not in nums:
            return False

    return True