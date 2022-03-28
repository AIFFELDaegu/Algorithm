import heapq

def solution(operations):
    dpq = [] #dual priority queue
    for o in operations:
        # print(dpq)
        command, num = o.split()
        if command == "I":
            heapq.heappush(dpq, int(num))
        elif command == "D" and dpq:
            if num == '1' :
                dpq.pop(-1)
            elif num == '-1':
                heapq.heappop(dpq)

    return [max(dpq),min(dpq)] if dpq else [0,0]

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))