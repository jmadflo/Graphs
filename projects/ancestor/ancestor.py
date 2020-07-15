def earliest_ancestor(ancestors, starting_node):
    # verify at least one parent of the starting_node or else return -1
    queue = []
    parent = None
    for pair in ancestors:
        if starting_node == pair[1]:
            parent = pair
            break
    # print(parent)
    if parent == None:
        return -1
    queue.append(parent)
    while len(queue) > 0:
        # print(queue)
        node = queue.pop(0)
        parent = node[0]
        for pair in ancestors:
            if pair[1] == parent:
                queue.append(pair)
                break
    return parent