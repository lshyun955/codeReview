def solution(s, n):
    alp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]
    ALP = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
    x = list(s)
    for i in range(len(x)):
        if x[i] in alp:
            num = alp.index(x[i])
            x[i] = alp[(num + n) % 26]
        elif x[i] in ALP:
            num = ALP.index(x[i])
            x[i] = ALP[(num + n) % 26]

    answer = "".join(x)
    return answer

