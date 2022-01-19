def solution(nums):
    nums.sort()
    answer = []
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                number = nums[i] + nums[j] + nums[k]
                n = 2
                while (number // 2) + 1 > n:
                    if number % n == 0:
                        break
                    if number // 2 == n:
                        answer.append(number)
                    n = n + 1

    return len(answer)

solution([1,2,3,4])