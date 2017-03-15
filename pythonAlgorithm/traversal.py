from collections import deque


# Walking Through a Connected Component of a Graph Represented Using Adjacency Sets
def walk(G, s, S=set()):					# Walk the graph from node s
	P, Q = dict(), set()					# Predecessors + "to do" queue
	P[s] = None								# s has no predecessor
	Q.add(s)								# We plan on starting with s
	while Q:								# Still nodes to visit
		u = Q.pop()							# Pick one, arbitrarily
		for v in G[u].difference(P, S):		# new nodes?
			Q.add(v)						# We plan to visit them!
			P[v] = u						# Remember where we came from
	return P								# The traversal tree


# Finding Connected Components
def component(G):						# the connected components
	comp = []
	seen = set()
	for u in G:
		if u in seen: continue
		C = walk(G, u)
		seen.update(C)
		comp.append(C)
	return comp


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
	if S is None: S = set()  # Initialize the history
	d[s] = t;
	t += 1  # Set discover time
	S.add(s)  # We've visited s
	for u in G[s]:  # Explore neighbors
		if u in S: continue  # Already visited. Skip
		t = dfs(G, u, d, f, S, t)  # Recurse; update timestamp
	f[s] = t;
	t += 1  # Set finish time
	return t  # return timestamp


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


# Iterative Deepening Depth-First Search
def iddfs(G, s):
	yielded = set()  # visited for the first time

	def recurse(G, s, d, S=None):  # Depth-limited DFS
		if s not in yielded:
			yield s
			yielded.add(s)
		if d == 0: return  # Max depth zero: backtrack
		if S is None: S = set()
		S.add(s)
		for u in G[s]:
			if u in S: continue
			for v in recurse(G, u, d - 1, S):  # Recurse with depth-1
				yield v

	n = len(G)
	for d in range(n):  # try all depths 0..V-1
		if len(yielded) == n: break  # All nodes seen?
		for u in recurse(G, s, d):
			yield u


# Breadth-First Search
def bfs(G, s):
	P, Q = {s:None}, deque([s])		# Parents and FIFO queue
	while Q:
		u = Q.popleft()				# constant-time for deque
		for v in G[u]:
			if v in P: continue		# Already has parent
			P[v] = u				# Reached from u: u is parent
			Q.append(v)
	return P


# Kosaraju's Algorithm for Finding Strongly Connected Components
def tr(G):							# Transpose (rev. edges of) G
	GT = {}
	for u in G: GT[u] = set()		# Get all the nodes in there
	for u in G:
		for v in G[u]:
			GT[v].add(u)			# Add all reverse edges
	return GT

def scc(G):
	GT = tr(G)						# Get the transposed graph
	sccs, seen = [], set()
	for u in dfs_topsort(G):		# DFS starting points
		if u in seen: continue		# Ignore covered nodes
		C = walk(GT, u, seen)		# Don't go "backward" (seen)
		seen.update(C)				# We've now seen C
		sccs.append(C)				# Another SCC found
	return sccs


