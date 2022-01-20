#TODO
# 0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다.
# numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.

#TODO 조건
# 1 ≤ numbers의 길이 ≤ 9
# 0 ≤ numbers의 모든 원소 ≤ 9
# numbers의 모든 원소는 서로 다릅니다.

#TODO 입출력 예
# [1,2,3,4,6,7,8,0]	14
# [5,8,4,0,6,7,9]	6

def solution(numbers):
    full = [0,1,2,3,4,5,6,7,8,9]
    none = []
    numbers.sort()
    for int in full:
        if int not in numbers:
            none.append(int)
    return sum(none)


solution([1,2,3,4,6,7,8,0])