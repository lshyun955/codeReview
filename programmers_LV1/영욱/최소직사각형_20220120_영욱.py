def solution(sizes):
    small = 0
    big = 0
    for size in sizes:
        size.sort()
        if max(size) > big:
            big = max(size)
        if min(size) > small:
            small = min(size)
    return big * small



    answer = []
    return answer



solution([[60, 50], [30, 70], [60, 30], [80, 40]])