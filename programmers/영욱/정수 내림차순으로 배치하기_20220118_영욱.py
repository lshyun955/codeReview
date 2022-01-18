def solution(n):
    A = list(str(n))
    A.sort(reverse=True)
    answer = ""
    for a in A:
        answer = answer + a
    answer = int(answer)
    return answer

solution(12345667)

def solution2(n):
    A = list(str(n))
    A.sort(reverse=True)
    return int("".join(A))

solution2(12345667)