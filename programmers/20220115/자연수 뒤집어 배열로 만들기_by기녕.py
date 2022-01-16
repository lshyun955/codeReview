
n = 12345

def solution(n):
  a = [] # 빈 리스트
  a = list(map(int, str(n)[::-1])) # 문자열로 바꾸어 슬라이싱 반대로 하고 map으로 숫자열 변경 list에 담음
  return a
print(solution(n))