def solution(s):
    a = s.lower()
    if a.count('p') != a.count('y'):
        return False
    
    return True
