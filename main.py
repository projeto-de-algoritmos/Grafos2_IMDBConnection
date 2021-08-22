from itertools import permutations

graph = {
    'v1': ['v4', 'v5', 'v7'],
    'v2': ['v3', 'v5', 'v6'],
    'v3': ['v4', 'v5'],
    'v4': ['v5'],
    'v5': ['v7'],
    'v6': ['v7'],
    'v7': []
}

def adj_list(graph):
    graph_keys = graph.keys()
    graph_values = graph.values()

    list_values = []
    for sublist in graph_values:
        for item in sublist:
            list_values.append(item)

    count_dict = {}

    for key in graph_keys:
        count_dict[key] = list_values.count(key)

    return count_dict

def topological_ordering(graph):
    return_list = []
    list = adj_list(graph)
    min_value = min(list.values())
    print("Grafo inicial:",graph)
    candidates_all = [k for k, v in list.items() if v==min_value]

    print(candidates_all)

    for i in permutations(candidates_all):

        candidates = []
        for z in i: 
            candidates.append(z)

        while len(candidates) != 0:
            print("Candidatos:",candidates)
            return_list.append(candidates[0])
            to_att = graph[candidates[0]]
            for item in to_att:
                list[item] = list[item] - 1
                print("Count:",list[item])
                if list[item] == 0:
                    candidates.append(item)

            del graph[candidates[0]]
            del candidates[0]
            print("Grafo:",graph)

        print("rl",return_list)


topological_ordering(graph)  