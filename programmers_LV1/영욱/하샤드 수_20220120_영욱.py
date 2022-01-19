def solution(x):
    a = sum(int(i) for i in list(str(x)))

    if x % a == 0:
        print("True")
        return True
    else:
        print("False")
        return False