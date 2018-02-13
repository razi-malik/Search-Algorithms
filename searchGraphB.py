#!/usr/bin/env python

'''
Search - Graph:

Breadth-first 

'''
def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            newNode = list(set(graph[node]) - set(visited))
            queue.extend(newNode)
    return visited

def bfsPaths(graph, start, end):
    queue = [(start, [start])]
    while queue:
        (node, path) = queue.pop(0)
        for newNode in graph[node] - set(path):
            if newNode == end:
                yield path + [newNode]
            else:
                queue.append((newNode, path + [newNode]))

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

graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

graph2 = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print bfs(graph,'D')

print list(bfsPaths(graph2,'A','E'))
print list(bfsPaths(graph2,'B','F'))


'''
Old code with set:

def bfs(graph, start):
    #visited, queue = set(), [start]
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node] - visited)
    return visited
'''







