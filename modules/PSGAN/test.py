def solution(participant, completion):
    answer = []
    for i in range(len(participant)):
        if participant[i] in completion:
            completion.remove(participant[i])
            pass
        else:
            answer.append(participant[i])
    return answer

participant = ['mislav', 'stanko', 'mislav', 'ana']

completion = ['stanko', 'ana', 'mislav']

s = solution(participant,completion)
print(s)