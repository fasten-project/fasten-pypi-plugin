# Find path from given start node in Stiched Call Graph.



class DepthFirstSearch:

    @classmethod
    def depthFirstSearch(cls, adjList, startNode):

        cls.count = 0
        cls.adjList = adjList
        nodes = cls.adjList.getNodes()
        edges = cls.adjList.getEdges()
        print("Number of nodes:")
        print(nodes)
        print("Number of edges:")
        print(edges)
        cls.marked = [False] * nodes
        print(type(cls.marked))
        cls.dfs(startNode)
        print(cls.marked)
        print(cls.count)

        return cls.marked

    @classmethod
    def dfs(cls, currentNode):
        cls.marked[currentNode] = True
        cls.count += 1
#        adj = adjList.getAdjacencyList(currentNode)

        for w in cls.adjList.getAdjacencyList(currentNode):

            if not cls.marked[w]:
                cls.dfs(w)
