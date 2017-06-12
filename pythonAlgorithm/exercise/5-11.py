# coding：utf-8
from collections import deque


def bfs(G, s):
	seen, q, distance = set(), deque((s,'0')), dict()
	dist = 0
	while q:
		u = q.popleft()
		if u == '0':
			dist += 1
			continue
		if u in seen:
			continue
		distance[u] = dist
		seen.add(u)
		print u
		for v in G[u]:
			q.append(v)
		q.append('0')
	print distance


def bfs2(G, s):
	p, q = {s: 0}, deque(s)			# q代表父节点记录离起始点的距离
	while q:
		u = q.popleft()
		print u
		for v in G[u]:
			if v in p:
				continue
			p[v] = p[u]+1
			q.append(v)
	print p


if __name__ == "__main__":
	G = {
		'1': set('26'),
		'2': set('1345'),
		'3': set('24'),
		'4': set('325'),
		'5': set('24'),
		'6': set('1')
	}
	bfs(G, '1')
	bfs2(G, '1')
