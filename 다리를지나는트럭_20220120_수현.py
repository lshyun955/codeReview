import collections
# bridge_length = 100   weight = 100  truck_weights = [10,10,10,10,10,10,10,10,10,10]
def solution(bridge_length, weight, truck_weights):
    truck_weights = collections.deque(truck_weights)
    length = collections.deque([0 for _ in range(bridge_length)])
    time = 0
    
    while truck_weights:
        curTruck = truck_weights.popleft()
        
        if curTruck + sum(length) <= weight:
            length.append(curTruck)
            length.popleft()
            time += 1
            print('if :', length)
        else:
            lenghtSum = sum(length)
            while lenghtSum + curTruck > weight:
                length.append(0)
                lenghtSum -= length.popleft()
                time += 1
            length[-1] = curTruck
        
                
                        
    return time + bridge_length