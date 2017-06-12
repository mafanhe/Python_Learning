N,M = [int(_) for _ in raw_input().split()]
n = []
m = []
for i in range(N):
	n.append(raw_input())
for i in range(M):
	m.append(raw_input())
l = [set(s.split()) for s in n]
w = [set(s.split()) for s in m]
score = [[]for i in range(N)]
for i in range(M):
	for j in range(N):
		# print w[i]
		# print l[j]
		# print w[i]&l[j]
		# print
		score[i].append(len(w[i]&l[j]))
no = []
# print l,w,score
for i in range(M):
	no.append(score[i].index(max(score[i])))
# print no
for i in no:
	print n[i]