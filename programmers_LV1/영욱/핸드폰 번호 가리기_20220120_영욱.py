def solution(phone_number):
    a = list(phone_number)

    answer = ""
    for i in range(len(a)-4):
        a[i] = "*"
        answer = answer + a[i]
    for i in range(len(a)-4,len(a)):
        answer = answer + a[i]

    return answer

solution("01033334444")