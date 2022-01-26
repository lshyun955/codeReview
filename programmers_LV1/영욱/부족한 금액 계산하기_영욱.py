def solution(price, money, count):
    cost = 0
    for i in range(1,count + 1):
        pay = i * price
        cost += pay
    if cost > money:
        return cost - money
    else:
        return 0