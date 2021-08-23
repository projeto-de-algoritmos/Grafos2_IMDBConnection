def BFS_SP(graph, start, target):
    explored = []
     
    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]
     
    # If the desired node is
    # reached
    if start == target:
        print("Same Node")
        return
     
    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]
         
        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]
             
            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour["name"])
                queue.append(new_path)
                 
                # Condition to check if the
                # neighbour node is the target
                if neighbour["name"] == target:
                    return new_path

            explored.append(node)
 
    # Condition when the nodes
    # are not connected

    return []


def dijkstra(graph, start, target):
    distances = {}

    for actor, connections_list in graph.items():
        actor_distances = {}
        for other_actor in connections_list:
            actor_distances[other_actor["name"]] = 1/len(other_actor["shared_movies"])

        distances[actor] = actor_distances


    shortest_distance = {}
    predecessor = {}
    unseen_nodes = distances
    infinity = 999999999999999
    path = []

    for node in unseen_nodes:
        shortest_distance[node] = infinity

    shortest_distance[start] = 0
    
    while unseen_nodes:
        min_node = None
        for node in unseen_nodes:
            if min_node is None:
                min_node = node
            elif shortest_distance[node] < shortest_distance[min_node]:
                min_node = node

        for child_node, weight in distances[min_node].items():
            if weight + shortest_distance[min_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_node]
                predecessor[child_node] = min_node

        unseen_nodes.pop(min_node)

    current_node = target

    while current_node != start: 
        path.insert(0, current_node)
        current_node = predecessor[current_node]

    path.insert(0, start)

    if shortest_distance[target] != infinity:
        return path

    else:
        return []
        


    