# Recursive Depth-First Search
def rec_dfs(G, s, S=None):
	if S is None: S = set()
	S.add(s)
	for u in G[s]:
		if u in S: continue
		rec_dfs(G, s, S)


# Iterative Depth-First Search
def iter_dfs(G, s):
	S, Q = set(), []
	Q.append(s)
	while Q:
		u = Q.pop()
		if u in S: continue
		S.add(u)
		Q.extend(G[u])
		yield u


# A General Graph Traversal Function
def traverse(G, s, qtype=set):
	S, Q = set(), qtype()
	Q.add(s)
	while Q:
		u = Q.pop()
		if u in S: continue
		for v in G[u]:
			Q.add(v)
		yield u


# depth-first Search with Timestamps
def dfs(G, s, d, f, S=None, t=0):
	if S is None: S = set()				# Initialize the history
	d[s] = t; t += 1					# Set discover time
	S.add(s)							# We've visited s
	for u in G[s]:						# Explore neighbors
		if u in S: continue				# Already visited. Skip
		t = dfs(G, u, d, f, S, t)		# Recurse; update timestamp
	f[s] = t; t += 1					# Set finish time
	return t							# return timestamp


# Topological Sorting Based on Depth-First Search
def dfs_topsort(G):
	S, res = set(), []
	def recurse(u):
		if u in S: return
		S.add(u)
		for v in G[u]:
			recurse(v)
		res.append(u)
	for u in G:
		recurse(u)
	res.reverse()
	return res




