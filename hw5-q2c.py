import sys


def bellmanford_algo(graph, src, dest):
    largest_value = sys.maxsize
    node_lenght = {
        'a': {'cost': largest_value, 'pred': []},
        'b': {'cost': largest_value, 'pred': []},
        'c': {'cost': largest_value, 'pred': []},
        'd': {'cost': largest_value, 'pred': []},
        'e': {'cost': largest_value, 'pred': []},
        'f': {'cost': largest_value, 'pred': []},
        'g': {'cost': largest_value, 'pred': []},
        'h': {'cost': largest_value, 'pred': []},
        'j': {'cost': largest_value, 'pred': []},
        'k': {'cost': largest_value, 'pred': []}
    }
    node_lenght[src]['cost'] = 0

    for i in range(10):

        for itration in graph:
            for neighbor_node in graph[itration]:
                cost = node_lenght[itration]['cost'] + graph[itration][neighbor_node]
                if cost < node_lenght[neighbor_node]['cost']:
                    node_lenght[neighbor_node]['cost'] = cost
                    if node_lenght[neighbor_node]['cost'] == largest_value:
                        node_lenght[neighbor_node]['pred'] = node_lenght[itration]['pred'] + [itration]
                    else:
                        node_lenght[neighbor_node]['pred'].clear()
                        node_lenght[neighbor_node]['pred'] = node_lenght[itration]['pred'] + [itration]

    print("Shortest interval : " + str(node_lenght[dest]['cost']))
    print("Shortest Path from source to destination : " + str(node_lenght[dest]['pred']))


graph = {
    'a': {'b': 1, 'e': 1},
    'b': {'c': 1, 'a': 1},
    'c': {'b': 1, 'j': 4, 'f': 3, 'g': 1},
    'd': {'j': 2, 'k': 1, 'e': 5, 'h': 1},
    'e': {'g': 1, 'a': 1, 'd': 5},
    'f': {'c': 3, 'k': 1},
    'g': {'e': 1, 'h': 1, 'c': 1},
    'h': {'g': 1, 'd': 1},
    'j': {'c': 4, 'd': 2},
    'k': {'f': 1, 'd': 1}
}

source = input("enter the source node of the graph:: ")
destination = input("Enter the end node of the graph :: ")
print()
print()
bellmanford_algo(graph, source, destination)
