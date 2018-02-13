#!/usr/bin/env python

'''
Graph Search:

Depth-first Search
'''

def dfsPaths(graph, start, end):
	path = []
	dfs(graph, start, end, [], path)
	return path

def dfs(graph, start, end, visited, path):
	visited += [start]
	if start == end:
		path.append(visited)
	else:
		for node in graph[start]:
			if node not in visited:
				dfs(graph, node, end, visited[:], path)


graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

'''
The Graph: 
	  A
	 /  \
	C	  B
	|	 /	\
	|  D	 E
	 \ 	/
	  \  /
	   F	 
'''

print dfsPaths(graph,'A','E')
print dfsPaths(graph,'B','F')


# DFS Iterative, if have time!
def dfsIterative(graph, start):
	stack = [start]
	path = []
	while stack:
		start = stack.pop()
		if start in path:
			continue
		path.append(start)
		for neighbor in graph[start]:
			stack.append(neighbor)
	return path

#print dfsIterative(graph, 'A')















