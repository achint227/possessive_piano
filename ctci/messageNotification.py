def showNotification(message, k):
    if k >= len(message):
        return message

    words = message.split()
    currLen = 0

    return words, currLen


def solution(arr):
    queue = [(i, arr[i]) for i in range(len(arr))]
    curr_time, res = 0, 0
    while queue:
        a = len(queue)

        while a:
            i, elem = queue.popleft()
            curr_time += 1
            elem -= 1
            if elem:
                queue.append((i, elem))
            else:
                res += curr_time

            a -= 1
    return res
