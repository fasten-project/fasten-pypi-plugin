# Create adjacency list for Stitched Call Graph.

import json


class CreateAdjacencyList:

    @classmethod
    def createAdjacencyList(cls, stitched_call_graph):

#       Read the list of calls from Stitched Call Graph.
        print("Read the list of calls from the Stitched Call Graph:")
        with open(stitched_call_graph) as f:
            scg = json.loads(f.read())

        cls.verticesPair = scg["edges"]
        cls.edges = len(scg["edges"])
        print("Vertices pairs:")
        print(cls.verticesPair)
        print("Number of Edges:")
        print(cls.edges)
        print("Number of Vertices:")
        cls.vertices = cls.getNumberOfVertices() + 1
        print(cls.vertices)

        cls.graph = [None] * cls.vertices
        cls.addEdges()
        cls.print_agraph()


#   Add edges to adjacency list.
    @classmethod
    def addEdges(cls):

        for pair in cls.verticesPair:

            vertex = AdjNode(pair[0])
            vertex.next = cls.graph[pair[1]]
            cls.graph[pair[1]] = vertex
            vertex = AdjNode(pair[1])
            vertex.next = cls.graph[pair[0]]
            cls.graph[pair[0]] = vertex


#   Print adjacency list.
    @classmethod
    def print_agraph(cls):

        cls.adj = {}

        for i in range(cls.vertices): # 0 -> 13
            print(str(i) + ":", end="")
            temp = cls.graph[i]
            cls.adj[i] = []

            while temp:
                cls.adj[i].append(int("{}".format(temp.vertex)))
                print(" {}".format(temp.vertex), end="")
                temp = temp.next
            print("")

        print(cls.adj)
        print(cls.graph[0])


#   Get number of vertices existent in the Stitched Call Graph.
    @classmethod
    def getNumberOfVertices(cls):

        vertices = 0

        for pair in cls.verticesPair:
            if pair[0] > vertices:
                vertices = pair[0]
            if pair[1] > vertices:
                vertices = pair[1]
        return vertices


#   Return number of vertices.
    @classmethod
    def getVertices(cls):
        return  cls.vertices


#   Return number of edges.
    @classmethod
    def getEdges(cls):
        return  cls.edges


#   Return adjacency list:
    @classmethod
    def getAdjacencyList(cls, vertex):
        print(cls.adj[vertex])
        return  cls.adj[vertex]


class AdjNode:

    def __init__(self, value):

        self.vertex = value
        self.next = None
