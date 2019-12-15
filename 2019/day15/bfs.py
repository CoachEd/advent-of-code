from pprint import pprint

# pos is (row, column), not (x, y)
class Node:
    def __init__(self, val, pos):
        self.val = val
        # Position info is stored here and ALSO as index in graph -
        # this is a form of data duplication, which is evil!
        self.pos = pos
        self.visited = False
    def __repr__(self):
        # nice repr for pprint
        return repr(self.pos)

# You had mistake here, "arena" instead of "graph"
# Before posting questions on stackoverflow, make sure your examples
# at least produce some incorrect result, not just crash.
# Don't make people fix syntax errors for you!
def bfs(graph, start):
    fringe = [[start]]
    # Special case: start == goal
    if start.val == 'g':
        return [start]
    start.visited = True
    # Calculate width and height dynamically. We assume that "graph" is dense.
    width = len(graph[0])
    height = len(graph)
    # List of possible moves: up, down, left, right.
    # You can even add chess horse move here!
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while fringe:
        # Print fringe at each step
        #pprint(fringe)
        #print('')
        # Get first path from fringe and extend it by possible moves.
        path = fringe.pop(0)
        node = path[-1]
        pos = node.pos
        # Using moves list (without all those if's with +1, -1 etc.) has huge benefit:
        # moving logic is not duplicated. It will save you from many silly errors.
        # The example of such silly error in your code:
        # graph[pos[0-1]][pos[1]].visited = True
        #           ^^^
        # Also, having one piece of code instead of four copypasted pieces
        # will make algorithm much easier to change (e.g. if you want to move diagonally).
        for move in moves:
            # Check out of bounds. Note that it's the ONLY place where we check it. Simple and reliable!
            if not (0 <= pos[0] + move[0] < height and 0 <= pos[1] + move[1] < width):
                continue
            neighbor = graph[pos[0] + move[0]][pos[1] + move[1]]
            if neighbor.val == 'g':
                return path + [neighbor]
            elif neighbor.val == 'o' and not neighbor.visited:
                # In your original code there was a line:
                # if neighbor is not neighbor.visited:
                # which was completely wrong. Read about "is" operator.
                neighbor.visited = True
                fringe.append(path + [neighbor])  # creates copy of list
    raise Exception('Path not found!')


# MAIN

# Graph in convenient form: 0 is empty, 1 is wall, 2 is goal.
# Note that you can have multiple goals.
s = """##################################################
##########.#...#...#.........#.#.......#...#...#.#
##########.#.#.#.#.#.###.###.#.#.#.###.#.#.#.#.#.#
##########...#...#...###.#...#...#...#...#...#.#.#
##########.#############.#.#########.#########.#.#
##########...#.....#####.#.........#.#.......#...#
############.#.###.#####.#########.#.#######.###.#
##########.....###..####.#.....#...#.#...#.....#.#
##########.#############.#.###.#.###.#.#.#.#####.#
##########.#...#####.....#.###.#.#...#.#.#...#...#
############.#.#####.#####.#####.#.###.#.###.#.###
##########...#.#.....#.....#####.#.#...#...#.....#
##########.###.#.#######.#######.#.#.#####.#.#####
##########...#.#...#####.#######.#.#.#...#.#.#...#
##########.#.#.#.#.#####.#######.#.#.###.#.###.#.#
##########.#.#.#.#.....#...#####.#.#.#...#.....#.#
##########.#.#.#######.#.#.#####.#.#.#.#########.#
##########.#.#.........#.#.###.....#.#.#...#.....#
############.###########.#.###.#####.#.#.#.#.#####
##########...###.........#.....#...#.#...#.#.....#
##########.#####################.#.#.#.###.#####.#
##########.......#.......#...#S..#...#.###.....#.#
##########.#####.#.#####.#.#.#########.#######.#.#
##########...#...#.....#...#.......#...#######...#
############.#.#.#####.###########.#.#############
##########...#.#.#.....#.......#...#.#############
##########.###.#.#.#####.#######.###.#############
##########.#...#.#...#.#.....###.#...#####.#######
############.###.###.#.#.###.###.#.#######.#######
##########...#...#.#.#.#...#.###...#######.###...#
##########.###.###.#.#.###.#.#############.###.#.#
##########.#.#.#...#.#.#...#...........###.....#.#
##########.#.#.#.#.#.#.#.#####.#####.#.###.#####.#
##########.#.#...#.#.#...#...#...#...#...#.....#.#
##########.#.#####.#.#####.#.###.#.#####.###.###.#
##########.#.#.....#.#.....#.#...#.#...#.#@..#...#
##########.#.#.#####.#.#####.#####.#.#.#.#####.#.#
##########.#.....#...#.#.#...#...#...#.#.....#.#.#
##########.#######.###.#.#.###.#.#####.#####.#.#.#
##########.............#.......#.......#.......#.#
##################################################
"""


#WORKS
#s = """######
##...@#
##..###
##..#S#
##....#
#######
#"""


arr = s.split('\n')[:-1]
graph = []
starty = -1
startx = -1
targety = -1
targetx = -1
# Graph in convenient form: 0 is empty, 1 is wall, 2 is goal.
for y in range(0,len(arr)):
    temparr = []
    for x in range(0,len(arr[y])):
        c = arr[y][x]
        if c == ' ' or c == '#':
            temparr.append(1)
        elif c == '.':
            temparr.append(0)
        elif c == '@':
            temparr.append(2)
            targety = y
            targetx = x
        elif c == 'S':
            starty = y
            startx = x
            temparr.append(0)
        else:
            temparr.append(1)
    graph.append(temparr)


"""
graph = [
    [0, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 2, 1]
]
"""





# Transform int matrix to Node matrix.
TRANSLATE = {0: 'o', 1: 'x', 2: 'g'}
graph = [[Node(TRANSLATE[x], (i, j)) for j, x in enumerate(row)] for i, row in enumerate(graph)]
# Find path
try:
    #path = bfs(graph, graph[0][0])  # y,x
    path = bfs(graph, graph[starty][startx])

    print("Path found: {!r}".format(path))
    print('starty,startx   ' + str(starty) + ',' + str(startx))
    print('targety,targetx ' + str(targety) + ',' + str(targetx))
    print("# of instructions: " + str(len(path) - 1))
except Exception as ex:
    # Learn to use exceptions. In your original code, "no path" situation
    # is not handled at all!
    print(ex)