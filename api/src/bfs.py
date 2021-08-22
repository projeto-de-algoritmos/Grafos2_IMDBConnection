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