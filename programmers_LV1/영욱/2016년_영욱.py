def solution(a, b):
    month = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    date = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    days = b + sum(month[0:a])
    return date[days%7]