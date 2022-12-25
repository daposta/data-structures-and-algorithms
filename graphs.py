graph_data = {
    'a':['b','c'],
    'b':['d'],
    'c': ['e'],
    'd':['f'],
    'e':[],
    'f': []
}

def depthFirstGraph(graph, start):
    
    stack = [start]

    while len(stack)> 0:
        current = stack.pop()
        for neighbor in graph[current]:
            stack.append(neighbor)
    
def depthFirstGraphRecursion(graph, start):
    print(start)
    for neighbor in graph[start]:
        depthFirstGraphRecursion(graph, neighbor)


# depthFirstGraph(graph_data, 'a')
# depthFirstGraphRecursion(graph_data, 'a')


graph_data2 = {
    'f':['g','i'],
    'g':['h'],
    'h':[],
    'i': ['g', 'k'],
    'j':['i'],
    'k':[],
}

def hasPath(graph, start, dest):
    
    queue = [start]

    while len(queue) > 0:
        current = queue.pop(0)
        if current == dest : return True
        for neighor in graph[current]:
            queue.append(neighor)
    return False



def hasPathRecursion(graph, start, dest):
    if start== dest:
        return True
    for neighbor in graph[start]:
        if not neighbor == dest:
            hasPathRecursion(graph, neighbor, dest)
        return True
    return False

# print(hasPath(graph_data2, 'f', 'k'))

#undirected graph
edges =[
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n'],

]

def convert_to_graph(edges):
    graph = {}
    
    for edge in edges:
        a, b = edge
        if not a in graph:
            graph[a] = []
        if not b in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph
        

def undirectedPath(edges, start, dest):
    graph = convert_to_graph(edges)
    # print(graph)
    return hasPathForUndirectedGraph(graph, start, dest, set())


def hasPathForUndirectedGraph(graph, start, dest, visited):
    
    if start == dest: return True

    if start in visited: return False
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor == dest: return True
        
        hasPathForUndirectedGraph(graph, neighbor, dest, visited)
    return False

# print(undirectedPath(edges, 'i', 'k'))

f = {
    0: [8, 1, 5], 
    1: [0], 
    5: [0 , 8], 
    8: [0, 5], 
    2: [3,4], 
    3: [2, 4], 
    4: [3, 2]
    }

def connectedComponentsCount(graph, ):
    visited = set()
    counter = 0 

    for node in graph:
        if(explore(graph, node, visited) == True):
            counter +=1
    return counter


def explore(graph, current, visited):
    if current in visited: return False
    visited.add(current)

    for neighbor in graph[current]:
        explore(graph, neighbor, visited)
    return True

# print(connectedComponentsCount(f))

def largest_component(graph):
    largest = 0
    visited = set()
    for node in graph:
        size = explore_largest_component(graph, node, visited)
        if largest < size : largest = size

    return largest

def explore_largest_component(graph, current_node, visited):
    if current_node in visited: return 0
    visited.add(current_node)
    size =1
    for neighbor in graph[current_node]:
        size += explore_largest_component(graph, neighbor, visited)
    return size

# print(largest_component(f))


edges =[
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v'],

]
def compute_shortest_path_in_graph(edges, start, dest):
    #interested in the number of edges instead of number of nodes
    #breadth-first traversal is the best approach for this
    #breadth-first = queue
    visited = set([start])
    graph = convert_to_graph(edges)
    if not start in graph : return -1
    queue  = [[start, 0]]
    while (len(queue) > 0):
        node, distance = queue.pop(0)
        if node == dest : return distance

        for neighbor in graph[node]:
            if not neighbor in visited: visited.add(neighbor)
            queue.append([neighbor, distance +1])
    return -1


print(compute_shortest_path_in_graph(edges, 'b', 'g'))