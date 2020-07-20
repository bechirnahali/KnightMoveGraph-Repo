def solution(maze):
    if len(maze) < 2 or len(maze) > 20 or len(maze[0]) < 2 or len(maze[0]) > 20:
        return 0
    map_start = bfs(maze, [0, 0])
    map_end = bfs(maze, [len(maze) - 1, len(maze[0]) - 1])
    ones = getOnes(maze) # returns them in the form of strings

    #   print map_start
    #   print map_end
    #   print ones

    min = 1000 * 1000 * 1000
    for one in ones:
        adj1 = getAdj(one, map_start)
        adj2 = getAdj(one, map_end)
        if not adj1 or not adj2: # why double condition isn't it the same
            continue
        sum = adj1 + adj2 + 1
        if sum < min:
            min = sum

    # x = map_start[nodeToString([len(maze)-1, len(maze[0])-1])] if nodeToString([len(maze)-1, len(maze[0])-1]) in map_start else 0
    return min


def getAdj(one, map):
    l = []
    node = stringtoNode(one)
    x = node[0]
    y = node[1]
    a = nodeToString([x + 1, y])
    b = nodeToString([x - 1, y])
    c = nodeToString([x, y + 1])
    d = nodeToString([x, y - 1])

    if a in map:
        l.append(map[a]) # we are appending how many steps to go to visit this node
    if b in map:
        l.append(map[b]) #
    if c in map:
        l.append(map[c])
    if d in map:
        l.append(map[d])
    if len(l) == 0:
        return None
    else:
        return min(l) # the closest 0 neighbour to the one


def getOnes(maze):
    l = []
    for x in range(0, len(maze)):
        for y in range(0, len(maze[0])):
            #   print x
            #   print y
            if maze[x][y] == 1:
                l.append(nodeToString([x, y]))
    return l

#fist is [0,0]
def bfs(maze, first):
    queue = []
    dict = {}
    queue.append(first)
    dict[nodeToString(first)] = 1 #It contains all 0 nodes and the number of nodes to get to them.
    # the key is 0_0
    while len(queue) > 0:

        current = queue.pop(0) #first element in the list
        print current

        # add valid nodes to queue
        for neighbor in getNeighbors(current, maze): #we start with each node and its neighbours
            if neighbor[0] < 0 or neighbor[0] > len(maze) - 1 or neighbor[1] < 0 or neighbor[1] > len(maze[0]) - 1:
                pass
            else:
                if maze[neighbor[0]][neighbor[1]] == 0 and nodeToString(neighbor) not in dict:
                    queue.append(neighbor)
                    dict[nodeToString(neighbor)] = dict[nodeToString(current)] + 1
                else:
                    pass
    return dict


def stringtoNode(s):
    a = s.split('-')
    return [int(a[0]), int(a[1])]


def nodeToString(node):
    test = str(node[0]) + '-' + str(node[1])
    return test


def getNeighbors(current, maze):
    x = current[0]
    y = current[1]
    neighbors = []

    neighbors.append([x + 1, y])
    neighbors.append([x, y + 1])
    neighbors.append([x - 1, y])
    neighbors.append([x, y - 1])

    return neighbors



if __name__=='__main__':
    #maze = [[0,0,0,1,1,1,0,0,0,0],[1,1,0,1,1,1,0,1,1,0],[1,1,0,0,0,0,0,1,1,0],[0,0,1,1,1,1,1,1,1,0],[0,0,1,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,0,0,0]]
    maze=[[0,0],[0,0]]
    print solution(maze)
