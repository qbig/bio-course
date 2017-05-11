import sys

"""
Sample Input:
0
4
0->1:7
0->2:4
2->3:2
1->4:1
3->4:3
Sample Output:
9
0->2->3->4
"""

lines = sys.stdin.readlines()

start = lines[0].strip()
end = lines[1].strip()

g = {}
weight = {}

for l in lines[2:]:
	from_node, seg = l.strip().split("->")
	to_node, w = seg.split(":")
	w = int(w)
	if from_node not in g:
		g[from_node] = [to_node]
	else:
		g[from_node].append(to_node)

	weight[(from_node, to_node)] = w

print("graph:")
print(g)

def toposort(graph, start, end):
	in_degree = {}
	for from_node in graph:
		if from_node not in in_degree:
				in_degree[from_node] = 0
		
		for to_node in graph[from_node]:
			if to_node not in in_degree:
				in_degree[to_node] = 1
			else:
				in_degree[to_node] += 1
	to_remove = []
	for node in in_degree.keys():
		if in_degree[node] == 0 and node != start:
			to_remove.append(node)
	
	print("in_degree:")
	print(in_degree)
	for node in to_remove:
		in_degree.pop(node)
		graph.pop(node)
	
	print("in_degree:")
	print(in_degree)

	result = []
	while end in in_degree:
		#print (in_degree)
		for node in in_degree:
			if in_degree[node] == 0:
				result.append(node)
				in_degree.pop(node)
				#print("popping: "+node)
				if node in graph:
					for to_node in graph[node]:
						in_degree[to_node] -= 1
				
				break

	return result

def longest_path(graph, weight, start, end):
	topo_path = toposort(graph, start, end)
	if topo_path[0] != start:
		print("toposort[0] != start!!!!!")
		return
	topo_path = topo_path[1:]
	prev = {}
	score = {}
	for second_node in graph[start]:
		score[second_node] = weight[(start, second_node)]
		prev[second_node] = start

	for topo_node in topo_path:
		if topo_node in graph:
			for to_node in graph[topo_node]:
				if to_node not in score or score[to_node] + weight[(topo_node, to_node)] > score[to_node]:
					prev[to_node] = topo_node
					score[to_node] = score[topo_node] + weight[(topo_node, to_node)]
	path = ""
	cursor = end
	while cursor in prev:
		path = cursor + path
		cursor = prev[cursor]
	path = start + path
	return score[end], path


score, path = longest_path(g, weight, start, end)
print(score)
print("->".join(path))



	