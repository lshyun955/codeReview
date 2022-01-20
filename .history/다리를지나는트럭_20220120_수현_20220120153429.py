import collections
def solution(bridge_length, weight, truck_weights):
    truck_weights = collections.deque(truck_weights)
    length = collections.deque([0 for _ in range(bridge_length)])
    total = 0
    time = 0
    
    while truck_weights:
        total -= length.popleft()
        print('first : ', total)
        if total + truck_weights[0] > weight:
            length.append(0)
        else:
            truck = truck_weights.popleft()
            length.append(truck)
            total += truck
            print('second', total)
            
        time += 1
    print(length)
    time += bridge_length
    
    return time