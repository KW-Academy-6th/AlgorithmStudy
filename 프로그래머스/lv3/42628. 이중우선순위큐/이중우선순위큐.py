from queue import PriorityQueue
import heapq

def solution(operations):
    two_way_priority_queue = PriorityQueue()

    for operation in operations:
        op, value = operation.split()
        value = int(value)

        if op == "I":
            two_way_priority_queue.put(-value)

        elif op == "D":
            if value == 1:
                if not two_way_priority_queue.empty():
                    heapq.heappop(two_way_priority_queue.queue)
            elif value == -1:
                if not two_way_priority_queue.empty():
                    temp = []
                    while two_way_priority_queue.qsize() > 1:
                        temp.append(two_way_priority_queue.get())
                    two_way_priority_queue.get()
                    
                    for item in temp:
                        two_way_priority_queue.put(item)

    answer = []

    if two_way_priority_queue.qsize() == 0:
        answer.extend([0, 0])
    else:
        answer.append(-two_way_priority_queue.get())
        while two_way_priority_queue.qsize() > 1:
            two_way_priority_queue.get()
        answer.append(-two_way_priority_queue.get())

    return answer