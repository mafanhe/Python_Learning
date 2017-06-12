def is_bipartite(G, C, u, c):
	C[u] = c
	for v in G[u]:
		if C.get(v) == c:
			return False
		if v not in C and not is_bipartite(G, C, v, -c):
			return False
	return True


def solve(G):
	for v in G:
		if not is_bipartite(G, dict(),v,1):
			print 'no'
			return
	print 'yes'

if __name__ == "__main__":
	G = {
		'1': set('26'),
		'2': set('1345'),
		'3': set('24'),
		'4': set('325'),
		'5': set('24'),
		'6': set('1')
	}
	G2 = {
		'1': set('26'),
		'2': set('135'),
		'3': set('246'),
		'4': set('35'),
		'5': set('24'),
		'6': set('13'),
	}
	solve(G)
	solve(G2)
