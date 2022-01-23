def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    for w in new_id:
        if w.isalnum() or w in '._-':
            answer += w
    
    while True:
        if '..' in answer:
            answer = answer.replace('..', '.')
        else: break
    
    if answer[0] == '.' or answer[-1] == '.':
        answer = answer.strip('.')
    
    if answer == '':
        answer += 'a'
    
    if len(answer) >= 16:
        answer = answer[0:15]
        if answer[-1] == '.':
            answer = answer.strip('.')
    # while True:
    #     if len(answer) <= 2:
    #         answer += answer[-1]
    #     else: break
    while len(answer) <= 2:
        answer += answer[-1]
        
    return answer