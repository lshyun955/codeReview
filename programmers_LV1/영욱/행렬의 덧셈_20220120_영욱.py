def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        s_answer = []
        for j in range(len(arr1[i])):

            s_answer.append(arr1[i][j] + arr2[i][j])
        answer.append(s_answer)

    return answer

solution([[1,2],[2,3]],[[3,4],[5,6]])

