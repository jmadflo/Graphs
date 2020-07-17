from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

print(f'Number of Rooms: {len(world.rooms)}')

return_direction = {'n': 's', 'e': 'w', 'w': 'e', 's': 'n'}
num_rooms_in_world = len(world.rooms)

def maze_navegator(player, prev_room = None, direction = None, graph = {}, path = []):
    # move in the direction given in the variable "direction" if not first move
    if prev_room != None:
        path.append(direction)
        player.travel(direction)
        current_room = player.current_room.id
    current_room = player.current_room.id
    # print(f"Current room: {current_room}")
    # Initialize values for the directions of the current room
    if current_room not in graph:
        graph[current_room] = {}
        adjacent_rooms = player.current_room.get_exits()
        for room in adjacent_rooms:
            graph[current_room][room] = "?"
       
    # Add the prev_room at the return direction and the current room at the cooresponding direction of the prev_room
    if prev_room != None:
        graph[prev_room][direction] = current_room
        graph[current_room][return_direction[direction]] = prev_room
    
    # depth first traversal method, should continue traveling until dead end is hit
    # recursion allows for not having to waste moves returning to fork in the road
    for direction in graph[current_room]:
        if graph[current_room][direction] == "?":
            maze_navegator(player, current_room, direction, graph, path)
            if num_rooms_in_world != len(graph.keys()):
                path.append(return_direction[direction])
                player.travel(return_direction[direction])
    return path

traversal_path = maze_navegator(player)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
