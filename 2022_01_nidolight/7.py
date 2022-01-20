
def solution(priorities, location):
    waiting_list = [[priorities[i], i] for i in range(len(priorities))]
    finished = []
    answer = []

    recursive(waiting_list,finished)

    for i, f in enumerate(finished):
        if f[1] == location:
            answer = i+1
    return answer

def recursive(waiting_list,finished):
    print(finished)
    for p in waiting_list:
        if waiting_list[0][0] < p[0]:
            waiting_list.append(waiting_list.pop(0))
            break
    
    if waiting_list[0][0] == max([i[0] for i in waiting_list]):
        finished.append(waiting_list.pop(0))
    
    if len(waiting_list)==0:
        return

    return recursive(waiting_list,finished)

print(solution(	[1, 1, 9, 1, 1, 1],0))



# def solution(priorities, location):
#     jobs = len(priorities)
#     answer = 0
#     cursor = 0
#     while True:
#         if max(priorities) == priorities[cursor%jobs]:
#             priorities[cursor%jobs] = 0
#             answer += 1
#             if cursor%jobs == location:
#                 break
#         cursor += 1   
#     return answer
