def earliest_ancestor(ancestors, starting_node):
    relationships = {} # keys are each value 
    for pair in ancestors:
        if pair[1] in relationships:
            relationships[pair[1]].add(pair[0])
        else:
            relationships[pair[1]] = {pair[0]}
        if pair[0] not in relationships: # makes sure highest generation ancestors have an empty set
            relationships[pair[0]] = set()
    # print(relationships)
    if len(relationships[starting_node]) == 0: # no ancestors
        return -1
    next_gen = {starting_node}
    while len(next_gen) > 0:
        current_gen = next_gen
        next_gen = set()
        for node in current_gen:
            next_gen = next_gen | relationships[node]
    return min(current_gen)