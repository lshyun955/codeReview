def solution(s):
    a = s.lower() # 소문자

    if a.count("p") == 0 and a.count("y") == 0: # 둘 다 0인가요?
        return True

    if a.count("p") != a.count("y"): # 갯수 비교
        return False

    return True