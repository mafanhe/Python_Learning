import pythonAlgorithm.traversal as pt


def dfs(G, s):
	seen, stack = set(), [s]
	firsttime, finishtime = dict(), dict()
	time = 0
	while stack:
		time += 1
		u = stack.pop()
		# print u
		if u in seen:
			finishtime[u] = time
		else:
			firsttime[u] = time
			finishtime[u] = time
			seen.add(u)
		children = []
		for v in G[u]:
			if v in seen:
				continue
			children.append(v)
		if len(children)>=1:
			stack.append(u)
		if children:
			stack.append(children[0])
	print firsttime,finishtime


def dfs2(G, s):
	seen, stack = set(), [(None, s)]
	firsttime, finishtime = dict(), dict()
	time = -1
	while stack:
		# print stack
		u = stack.pop()
		if u[1] is None:
			time+=1
			finishtime[u[0]] = time
			continue
		if u[1] in seen:
			continue
		# print u
		time += 1
		seen.add(u[1])
		firsttime[u[1]] = time
		if G[u[1]]:
			stack.append((u[1], None))
		for v in G[u[1]]:
			stack.append((u[1], v))
	print firsttime, finishtime


if __name__ == "__main__":
	G = {
		'1':set('26'),
		'2':set('1345'),
		'3':set('24'),
		'4':set('325'),
		'5':set('24'),
		'6':set('1')
	}
	print "iter_dfs1:"
	dfs(G, '2')
	print "iter_dfs2:"
	dfs2(G, '2')
	d, f = dict(), dict()
	pt.dfs(G,'2',d,f)
	print "rec_dfs:"
	print d,f
