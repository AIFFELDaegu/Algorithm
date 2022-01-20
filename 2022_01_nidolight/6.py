
# def solution(progresses, speeds):
#     finished = []

#     while(len(finished)!=len(progresses)):
#         progresses = [x+speeds[i] for i, x in enumerate(progresses)] #speeds만큼 각 프로세스 증가
    
#         for i, percentage in enumerate(progresses):
#             if percentage >= 100:
#                 progresses[i]=-1000
#                 finished.append(i)
    
#     return finished

def solution(progresses, speeds):
    answer = []
    days = 0
    count = 0

    while len(progresses) != 0:
        # print(progresses[0] + days * speeds[0])
        if progresses[0] + days * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0 
            days += 1    
    

    answer.append(count)

    return answer


print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))