# coding=utf-8


# Listing 4-7. A Naive Solution to the Celebrity Problem
# O(n^2)
def naive_celeb(G):
	n = len(G)
	for u in range(n):					# For every candidate
		for v in range(n):				# For everyone else
			if u == v: continue			# Same person? Skip.
			if G[u][v]: break 			# Candidate knows other
			if not G[v][u]: break		# Other doesn't know candidate
		else:
			return u					# No breaks? Celebrity!
	return None							# Couldn't find anyone


# Listing 4-8. A Solution to the Celebrity Problem
# O(n)
def celeb(G):
	n = len(G)
	u, v = 0, 1						# The first two
	for c in range(2, n+1):			# Other to check
		if G[u][v]: u = c			# u knows v? Replace u
		else:		v = c			# Otherwise, replace v
	if u == n:		c = v			# u was replaced last; use v
	else:			c = u			# Otherwise, u is a candidate
	for v in range(n):				# For everyone else...
		if c == v: continue			# Same person? Skip
		if G[c][v]: break			# Candidate knows other
		if not G[v][c]: break		# Other doesn't know candidate
	else:
		return c					# No breaks? Celebrity
	return None						# Couldn't find anyone


if __name__ == "__main__":
	from random import randrange
	n = 100
	G = [[randrange(2) for i in range(n)] for i in range(n)]
	c = randrange(n)
	print c
	for i in range(n):
		G[i][c] = True
		G[c][i] = False
	print naive_celeb(G)
	print celeb(G)