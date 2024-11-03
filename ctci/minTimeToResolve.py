from collections import deque


def minTimeToResolve(cache_size, cache_time, server_time, urls):

    cache = deque()
    cache_set = set()
    res = []
    for url in urls:
        if url in cache:
            res.append(cache_time)
        else:
            res.append(server_time)

            if len(cache_set) == cache_size:
                if len(cache) > 0:
                    cache_set.remove(cache.popleft())
            cache_set.add(url)
            cache.append(url)

    return res
