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
    return hasPathForUndirectedGraph(graph, start, dest, set())


def hasPathForUndirectedGraph(graph, start, dest, visited):
    
    if start == dest: return True

    if start in visited: return False
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor == dest: return True
        
        hasPathForUndirectedGraph(graph, neighbor, dest, visited)
    return False

print(undirectedPath(edges, 'i', 'k'))
