def solution(s):
    lst = list(s)
    upperlst = []
    lowerlst = []
    for i in range(len(lst)):
        if lst[i].isupper():
            upperlst.append(lst[i])
        else:
            lowerlst.append(lst[i])
    upperlst.sort(reverse=True)
    lowerlst.sort(reverse=True)

    answer1 = "".join(lowerlst)
    answer2 = "".join(upperlst)

    return answer1 + answer2