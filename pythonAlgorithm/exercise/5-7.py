import pythonAlgorithm.traversal as pt


def dfs(G, s):
	seen, stack = set(), [s]
	firsttime, finishtime = dict(), dict()
	time = 0
	node_branch = 0
	while stack:
		time += 1
		u = stack.pop()
		print u
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
	pass

if __name__ == "__main__":
	G = {
		'1':set('26'),
		'2':set('1345'),
		'3':set('24'),
		'4':set('325'),
		'5':set('24'),
		'6':set('1')
	}
	dfs(G, '1')
	d, f = dict(), dict()
	pt.dfs(G,'1',d,f)
	print d,f
