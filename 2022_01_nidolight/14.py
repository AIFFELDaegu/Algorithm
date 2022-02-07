

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i, k in enumerate(participant):
        if i == len(completion):
            return participant[i]
        elif k != completion[i]:
            return participant[i]


import collections
def solution1(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

def solution2(participant, completion):
    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if p != c:
            return p

    return participant[-1]


print(solution2(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

s0 = {1:0,2:1,3:2}
s1 = set(s0)
s2 = set({1:0})

T = s1-s2
for t in T:
    print({t: s0[t]})

s3 = set('abcdef')
s4 = set('ade')
print(s3 & s4)