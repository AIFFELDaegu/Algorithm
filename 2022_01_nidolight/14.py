

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i, k in enumerate(participant):
        if i == len(completion):
            return participant[i]
        elif k != completion[i]:
            return participant[i]


print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], [
      "josipa", "filipa", "marina", "nikola"]))
