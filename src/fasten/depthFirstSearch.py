# Find path from given entry point in Stiched Call Graph.

class DepthFirstSearch:

    @classmethod
    def depthFirstSearch(cls, adjList, entry_point, list_of_nodes):
        """Find longest path from given entry point in Stiched Call Graph."""

        cls.count = 0
        cls.adjList = adjList
        cls.list_of_nodes = list_of_nodes
        cls.dfs(entry_point)

        return cls.list_of_nodes

    @classmethod
    def dfs(cls, current_node):
        """Walk through graph from entry point and mark visited nodes."""

        cls.list_of_nodes[current_node] = True
        cls.count += 1

        for w in cls.adjList.getAdjacencyList(current_node):

            if not cls.list_of_nodes[w]:
                cls.dfs(w)
