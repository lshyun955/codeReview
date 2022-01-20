def solution(progresses, speeds):
    answer = []
    done = []

    while len(progresses) > 0:
        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i]

        if progresses[0] >= 100:
            for program in progresses:
                if program >= 100:
                    done.append("0")
                else:
                    break
        if len(done) >= 1:
            answer.append(len(done))
            del progresses[:len(done)]
            del speeds[:len(done)]
            done = list()

    return answer