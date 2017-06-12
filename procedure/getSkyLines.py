import bisect
from heapq import heappush, heappop

def findSkyLines(buildings):
	nodes = []
	for building in buildings:
		nodes.append([building[0],building[2]])
		nodes.append([building[1],-building[2]])
	nodes.sort()
	skyLines = []
	height = [0]
	for node in nodes:
		if node[1]>0 :
			if node[1]>=height[-1]:
				skyLines.append(node)
				height.append(node[1])
		else:
			height.remove(-node[1])
			if -node[1]>=height[-1]:
				skyLines.append([node[0],-node[1]])

			if height[-1]==0:
				skyLines.append([node[0],0])
			else:
				skyLines.append([node[0],height[-1]])
	res = []
	pre = None
	for sk in skyLines:
		if pre is None or sk[1]==0 or pre[1]==0:
			pre = sk
			continue
		if sk[1]==pre[1]:
			res.append([pre[0],sk[0],pre[1]])
		else:
			if pre[0] != sk[0]:
				res.append([pre[0],sk[0],pre[1]])
		pre = sk

	print skyLines
	print res

def findSKL(buildings):
	def addsky(pos, hei):
		if sky[-1][1] != hei:
			sky.append([pos, hei])


	sky = [[-1, 0]]

	# possible corner positions
	position = set([b[0] for b in buildings] + [b[1] for b in buildings])
	print position

	# live buildings
	live = []

	i = 0

	for t in sorted(position):

		# add the new buildings whose left side is lefter than position t
		while i < len(buildings) and buildings[i][0] <= t:
			heappush(live, (-buildings[i][2], buildings[i][1]))
			i += 1

		# remove the past buildings whose right side is lefter than position t
		while live and live[0][1] <= t:
			heappop(live)

		# pick the highest existing building at this moment
		h = -live[0][0] if live else 0
		addsky(t, h)

	return sky[1:]

if __name__ == "__main__":
	buildings = [[1,3,3],[2,4,4],[5,6,1]]
	buildings2 = [[1,10,3],[2,5,8],[7,9,8]]
	buildings3 = [[1,10,8],[2,5,3],[7,9,3]]
	events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
	print events
	# print findSKL(buildings)