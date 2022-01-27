def solution(numbers, target):
    cnt = 0

    def dfs_recur(index, sum):
        nonlocal cnt
        if index == len(numbers):  # 재귀 탈출조건 걸어주기
            if sum == target:
                print("good")
                cnt += 1
                return
            else:
                return

        num = numbers[index]
        plus_sum = sum + num
        minus_sum = sum - num

        dfs_recur(index + 1, plus_sum)
        dfs_recur(index + 1, minus_sum)

    dfs_recur(0, 0)

    return cnt