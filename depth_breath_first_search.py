graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
        

visited, stack = set(), ['A']
#value of stack is true
while stack:
	#pop removes and returns last element in last
	vertex = stack.pop()
	if vertex not in visited:
		visited.add(vertex)
		stack.extend(graph[vertex] - visited)
		print(vertex)
		print(visited)
		print(stack)


#DFS, makr the currrent vertex being viisted
#explore each adjacent vetex that is not include din the visited set

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def depth_first_search(graph,start):
	#set liste of visted nodes
	visited, stack = set(), [start]
	#value of stack is true
	while stack:
		vertex = stack.pop()
		if vertex not in visited:
			visited.add(vertex)
			stack.extend(graph[vertex] - visited)
		return(visited)

print(depth_first_search(graph,'A'))

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def depth_first_search_2(graph,start,visited=None):
	#check if none, and make empty set if so
	if visited is None:
		visited = set()
	#start with first node	
	visited.add(start)
	for next in graph[start] - visited:
		#reurse
		depth_first_search_2(graph,next,visited)
	return(visited)

print(depth_first_search_2(graph,"C"))

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

#get alll paths
def dfs_paths(graph,start,goal):
	stack = [(start,[start])]
	while stack:
		(vertex,path) = stack.pop()
		for next in graph[vertex] - set(path):
			if next == goal:
				yield path + [next]
			else: 
				stack.append((next,path+[next]))

print(list(dfs_paths(graph,"A","F")))				

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

#create function for breath first search
#finds shortest path

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

print(bfs(graph,"A"))

#create function for bfs
#fins all paths between start and end

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

#finds path and returns shortest
def bfs_paths(graph, start, goal):
	#create queueing vars
    queue = [(start, [start])]
    #as long as there is stuff to search
    while queue:
    	#remove from queue and check
        (vertex, path) = queue.pop(0)
        #remove node from path
        for next in graph[vertex] - set(path):
        	#stop at goal, and add to next to path
            if next == goal:
                yield list(path + [next])
            else:
                queue.append((next, path + [next]))

print(list(bfs_paths(graph, 'A', 'F')))

#different viersion of breath first search
def bfs_paths1(graph, start):
	visited,queue = set(), [start]
	while queue:
		vertex = queue.pop(0)
		if vertex not in visited:
			visited.add(vertex)
			queue.extend(graph[vertex] - visited)
	return(visited)










