# coding=utf8
# 拓扑排序


# Listing 4-9. A Naive Algorithm for Topological Sorting
def naive_topsort(G, S=None):
	if S is None: S = set(G)
	if len(S) == 1: return list(S)
	v = S.pop()
	seq = naive_topsort(G, S)
	min_i = 0
	for i, u in enumerate(seq):
		if v in G[u]: min_i = i+1
	seq.insert(min_i, v)
	return seq


# Listing 4-10. Topological Sorted of a Directed, Acyclic Graph
def topsort(G):
	count = dict((u, 0) for u in G)			# The in-degree for each node
	for u in G:
		for v in G[u]:
			count[v] += 1					# Count every in-edge
	Q = [u for u in G if count[u] == 0]		# Valid initial nodes
	S = []									# The result
	while Q:								# While we have start nodes...
		u = Q.pop()							# Pick one
		S.append(u)							# Use it as first of the rest
		for v in G[u]:
			count[v] -= 1					# "Uncount" its out-edges
			if count[v] == 0:				# New valid start nodes?
				Q.append(v)					# Deal with them next
	return S


if __name__ == "__main__":
	# G = {'a':{'b','f'},'b':{'c','d','f'},'c':{'d'},'d':{'f','e'},'e':{'f'},'f':{}}
	G = {'b':{'c','d','f'},'a':{'b','f'},'f':{},'d':{'f','e'},'c':{'d'},'e':{'f'}}
	print naive_topsort(G)
	print topsort(G)