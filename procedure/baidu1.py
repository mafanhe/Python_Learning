import sys
from collections import defaultdict
from Queue import Queue

time = input()
cnt = 1
while cnt <= time:
    n, m, s, t = [int(i) for i in sys.stdin.readline().strip().split()]
    lines = defaultdict(lambda: [])
    for _ in range(m):
        start, end, dist = [int(i) for i in sys.stdin.readline().strip().split()]
        lines[start].append((end, dist))
        lines[end].append((start, dist))
    queue = Queue()
    queue.put((s, tuple()))

    cost = [float('inf') for _ in range(n + 1)]
    cost[s] = 0
    paths = []
    while not queue.empty():
        p, path = queue.get()
        for end, dist in lines[p]:
            if end == t:
                paths.append((cost[p] + dist, max(path + (dist,))))
            if cost[p] + dist < cost[end]:
                queue.put((end, path + (dist,)))
                cost[end] = cost[p] + dist
    if len(paths) == 0:
        print 'Case #%d: No answer' % cnt
    else:
        re = sorted(paths, key=lambda x: (x[0], -x[1]))[0][1]
        print 'Case #%d: %d' % (cnt, re)
    cnt += 1