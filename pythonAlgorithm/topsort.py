# coding=utf8
# 拓扑排序


# A Naive Algorithm for Topological Sorting
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


if __name__ == "__main__":
	# G = {'a':{'b','f'},'b':{'c','d','f'},'c':{'d'},'d':{'f','e'},'e':{'f'},'f':{}}
	G = {'b':{'c','d','f'},'a':{'b','f'},'f':{},'d':{'f','e'},'c':{'d'},'e':{'f'}}
	print naive_topsort(G)