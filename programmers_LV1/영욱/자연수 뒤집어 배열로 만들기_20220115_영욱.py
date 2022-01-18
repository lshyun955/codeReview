def solution(n):
    string_n = str(n) # 숫자열 문자열 화

    list_n = list(string_n) # 문자열 리스트 화

    list_n.reverse() # 뒤집기

    for i in range(len(list_n)):
        list_n[i] = int(list_n[i]) # 문자열 숫자열 화

    answer = list_n # 끝

    return answer

