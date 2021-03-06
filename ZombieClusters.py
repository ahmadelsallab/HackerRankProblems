from Queue import Queue


def get_all_neighbors(G, S):
    candidates = G[S][:]

    neighbors = []
    # Find ones
    for i in range(len(candidates)):
        if candidates[i] == 1 and i != S:
            neighbors.append(i)
    return neighbors

Q = Queue()
visited = []
def traverseBFSRecursive(S, G):
    if not S in visited:
        #print S
        visited.append(S)
        neighbors = get_all_neighbors(G, S)


        # Queue all neighbors
        for neighbor in neighbors:
            Q.put(neighbor)
        '''
        try:
            next_node = Q.get(block=True)
            traverseBFSRecursive(next_node, G)
        except:
            return
        '''
        if not Q.empty():
            next_node = Q.get(block=True)
            traverseBFSRecursive(next_node, G)
        else:
            return
    else:
        '''
        try:
            next_node = Q.get(block=True)
            traverseBFSRecursive(next_node, G)
        except:
            return
        '''
        if not Q.empty():
            next_node = Q.get(block=True)
            traverseBFSRecursive(next_node, G)
        else:
            return
def traverseBFS(G):
    S = 0
    traverseBFSRecursive(S, G)

def getConnectedComponent(G):
    N = len(G)

    for node in range(N):

        if not node in visited:
            print 'Cluster starts at ', node
            traverseBFSRecursive(node, G)


def zombieCluster(zombies):
    N = len(zombies)

    nClusters = 0
    for node in range(N):

        if not node in visited:
            nClusters += 1
            traverseBFSRecursive(node, zombies)

    return nClusters

G = [[1,0,1],[0,1,0],[1,0,1]]
#traverseBFS(G)
#getConnectedComponent(G)
print zombieCluster(G)