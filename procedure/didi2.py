# -*- coding:utf-8 -*-
import sys

def findPath(graph, cur_pos, power, path):
    if cur_pos == (0, m - 1):
        global result
        if result is None or power>result[1]:
            result = (path, power)
    if power < 0:
        return
    x, y = cur_pos
    for dir_x, dir_y, p in [(-1, 0, 3), (1, 0, 0), (0, -1, 1), (0, 1, 1)]:
        if 0 <= x + dir_x < n and 0 <= y + dir_y < m and graph[x + dir_x][y + dir_y] == '1' and (
            x + dir_x, y + dir_y) not in visited and power - p >= 0:
            visited.add((x + dir_x, y + dir_y))
            findPath(graph, (x + dir_x, y + dir_y), power - p, path + ((x + dir_x, y + dir_y),))
            visited.remove((x + dir_x, y + dir_y))

for line in sys.stdin:
    n, m, p = [int(i) for i in line.strip().split()]
    graph = []
    for _ in range(n):
        graph.append([i for i in sys.stdin.next().strip().split()])
    results = []
    visited = set()
    visited.add((0, 0))
    result = None
    findPath(graph, (0, 0), p, ((0, 0),))
    if result is None:
        print 'Can not escape!'
    else:
        path =result[0]
        print ','.join(['['+str(x)+','+str(y)+']' for x, y in path])