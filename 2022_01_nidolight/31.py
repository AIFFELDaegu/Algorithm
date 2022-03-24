def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge_truck=[]
    bridge_time=[]

    while truck_weights or bridge_truck:
        # print(time,bridge_truck,truck_weights)
        time+=1
        bridge_time = [x+1 for x in bridge_time]
        if (len(bridge_time) >0
            and bridge_time[0] == bridge_length):
            bridge_truck.pop(0)
            bridge_time.pop(0)
        if (len(bridge_truck)-1<bridge_length
            and len(truck_weights) >0
            and weight >= sum(bridge_truck)+truck_weights[0]):
            bridge_truck.append(truck_weights.pop(0))
            bridge_time.append(0)

    return time

print(solution(2,10,[7,4,5,6]))
# print(solution(100	,100,	[10,10,10,10,10,10,10,10,10,10]))