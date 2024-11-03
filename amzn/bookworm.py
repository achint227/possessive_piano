from heapq import heappush, heappop

def buyVolumes(daily_volumes):

    req_book = 1

    pq = []

    res = []

    for v in daily_volumes:

        curr = []

        heappush(pq, v)

        while pq and pq[0] == req_book:
            curr.append(heappop(pq))
            req_book += 1
        
        
        res.append(curr if curr else [-1])
    
    return res


print(buyVolumes([1, 4, 3,7, 2, 6,5]))
print(buyVolumes([2, 1, 4, 3]))