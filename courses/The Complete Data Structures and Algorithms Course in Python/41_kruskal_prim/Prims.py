"""
Prims Algorithm  in Python

Time complexity: O(V^3)
Space complexity: O(V)
"""

import sys


class Graph:
    def __init__(self, vertexNum, edges, nodes):
        self.edges = edges
        self.nodes = nodes
        self.vertexNum = vertexNum
        self.MST = []

    def printSolution(self):
        print("Edge : Weight")
        path = self.MST[0][0]
        for s, d, w in self.MST:
            print("%s -> %s: %s" % (s, d, w))
            if d not in path:
                path += d
        print("path: ", path)

    def primsAlgo(self):
        visited = [0] * self.vertexNum
        edgeNum = 0
        visited[0] = True
        while edgeNum < self.vertexNum - 1:  # O(V)
            min = sys.maxsize
            for i in range(self.vertexNum):  # O(V)
                if visited[i]:
                    for j in range(self.vertexNum):  # O(V)
                        if (not visited[j]) and self.edges[i][j]:
                            if min > self.edges[i][j]:
                                min = self.edges[i][j]
                                s = i
                                d = j
            self.MST.append([self.nodes[s], self.nodes[d], self.edges[s][d]])
            visited[d] = True
            edgeNum += 1
        self.printSolution()


edges = [
    [0, 10, 20, 0, 0],
    [10, 0, 30, 5, 0],
    [20, 30, 0, 15, 6],
    [0, 5, 15, 0, 8],
    [0, 0, 6, 8, 0],
]
nodes = ["A", "B", "C", "D", "E"]
g = Graph(5, edges, nodes)
g.primsAlgo()
