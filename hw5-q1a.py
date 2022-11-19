short_dist = {}
prior = {}
unlimited = 9999999
path = []


def dijkstra_algo(graph, start, goal):
    unreachednode = graph
    for node in unreachednode:
        short_dist[node] = unlimited
    short_dist[start] = 0

    while unreachednode:
        minNode = None
        for node in unreachednode:
            if minNode is None:
                minNode = node
            elif short_dist[node] < short_dist[minNode]:
                minNode = node

        for childNode, weight in graph[minNode].items():
            if weight + short_dist[minNode] < short_dist[childNode]:
                short_dist[childNode] = weight + short_dist[minNode]
                prior[childNode] = minNode
        unreachednode.pop(minNode)

    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = prior[currentNode]
        except KeyError:
            print('Something wrong Path not reachable')
            break
    path.insert(0, start)
    if short_dist[goal] != unlimited:
        print('Shortest interval is ' + str(short_dist[goal]))
        print('And the path is ' + str(path))


# input from the user
starting_point = input("enter the source node of the graph:: ")
ending_pint = input("Enter the end node of the graph :: ")

print()
print()

# make a graph
graph = {
    's': {'a': 4, 'b': 6},
    'a': {'c': 2, 'd': 1},
    'b': {'a': 2, 'd': 2},
    'c': {'d': 1, 't': 3},
    'd': {'t': 7},
    't': {'t': 0}
}


dijkstra_algo(graph, starting_point, ending_pint)
