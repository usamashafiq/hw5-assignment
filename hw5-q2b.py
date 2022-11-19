import sys


def bellmanford_algo(graph, src, dest):
    largest_value = sys.maxsize
    node_lenght = {'a': {'cost': largest_value, 'pred': []},
                   'b': {'cost': largest_value, 'pred': []},
                   'c': {'cost': largest_value, 'pred': []},
                   'd': {'cost': largest_value, 'pred': []},
                   'e': {'cost': largest_value, 'pred': []},

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
    'a': {'b': 10, 'e': 5},
    'b': {'c': 1, 'e': 2},
    'c': {'b': 4},
    'd': {'a': 7, 'c': 6},
    'e': {'d': 2, 'b': 3, 'c': 9}}

source = input("enter the source node of the graph:: ")
destination = input("Enter the end node of the graph :: ")
print()
print()
bellmanford_algo(graph, source, destination)
