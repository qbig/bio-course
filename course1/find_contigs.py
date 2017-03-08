import sys

lines = [l.strip() for l in sys.stdin.readlines()]

"""
Algo: 
 EulerianCycle(Graph)
        form a cycle Cycle by randomly walking in Graph (don't visit the same edge twice!)
        while there are unexplored edges in Graph
            select a node newStart in Cycle with still unexplored edges
            form Cycle by traversing Cycle (starting at newStart) and then randomly walking 
            Cycle <- Cycle
        return Cycle

 Code Challenge: Solve the Eulerian Cycle Problem.
     Input: The adjacency list of an Eulerian directed graph.
     Output: An Eulerian cycle in this graph.

 Sample Input:
     0 -> 3
     1 -> 0
     2 -> 1,6
     3 -> 2
     4 -> 2
     5 -> 4
     6 -> 5,8
     7 -> 9
     8 -> 7
     9 -> 6

 Sample Output:
     6->8->7->9->6->5->4->2->1->0->3->2->6

"""

class DBGraph(object):

    def __init__(self, adjacencyList):
        #print adjacencyList
        self.adjacencyList = {}
        self.outDegree = {}
        self.inDegree = {}
        self.visited = {}
        self.nodes = set()
        for l in adjacencyList:
            startNode, endNodes = [l.strip() for l in l.split("->")]
            #print startNode, endNodes
            #print self.adjacencyList
            if startNode not in self.adjacencyList:
                self.adjacencyList[startNode] = endNodes.split(",")
                self.outDegree[startNode] = len(self.adjacencyList[startNode])
            else :
                self.adjacencyList[startNode] += endNodes.split(",")
                self.outDegree[startNode] = len(self.adjacencyList[startNode])
            # print "after,", self.adjacencyList
            if startNode not in self.nodes:
                self.nodes.add(startNode)
            
            for node in self.adjacencyList[startNode]:
                if node in self.inDegree:
                    self.inDegree[node] += 1
                else:
                    self.inDegree[node] = 1
                
                if node not in self.nodes:
                    self.nodes.add(node)
            for node in self.nodes:
                if node not in self.inDegree:
                    self.inDegree[node] = 0
                if node not in self.outDegree:
                    self.outDegree[node] = 0

        # print "final after,", self.adjacencyList
        # add a edge
        unbalanced = []
        for node in self.nodes:
            if node not in self.inDegree:
                unbalanced.append(node)
            elif node not in self.outDegree:
                unbalanced.append(node)
            else:
                if self.inDegree[node] != self.outDegree[node]:
                    unbalanced.append(node)

        # print "Out Degree: ",self.outDegree 
        # print "In Degree: ",self.inDegree
        # print self.adjacencyList

    def printGraph(self):
        for key in self.adjacencyList:
            print key, "->", self.adjacencyList[key]

    def getNext(self, currentNode):
        for node in self.adjacencyList[currentNode]:
            if (currentNode, node) not in self.visited and self.outDegree[currentNode] > 0:
                self.visited[(currentNode, node)] = True
                return node
        
        return -1

    # def findCycle(self, startNode, currentNode, resultArr):
    #     if currentNode == startNode:
    #         return resultArr 

    #     node = self.getNext(currentNode)
    #     resultArr.append(node)
    #     return self.findCycle(startNode, node, resultArr)

    def findCycle(self, startNode, currentNode, resultArr):
        while currentNode != startNode:
            node = self.getNext(currentNode)
            resultArr.append(node)
            currentNode = node

        return resultArr

        
        return self.findCycle(startNode, node, resultArr)

    def getUnfinishedNode(self, nodes):
        for index, node in enumerate(nodes):
            if self.outDegree[node] > 0:
                return index

        return -1

    def isOneInOneOut(self, node):
        return self.inDegree[node] == 1 and self.outDegree[node] == 1

    def findNonBranchingPaths(self):

        """
           MaximalNonBranchingPaths(Graph)
                Paths <- empty list
                for each node v in Graph
                    if v is not a 1-in-1-out node
                        if out(v) > 0
                            for each outgoing edge (v, w) from v
                                NonBranchingPath <- the path consisting of the single edge (v, w)
                                while w is a 1-in-1-out node
                                    extend NonBranchingPath by the outgoing edge (w, u) from w 
                                    w <- u
                                add NonBranchingPath to the set Paths
                for each isolated cycle Cycle in Graph
                    add Cycle to Paths
                return Paths
        """ 

        paths = []
        for node in self.adjacencyList.keys():
            if not self.isOneInOneOut(node) and self.outDegree[node] > 0:
                for toNode in self.adjacencyList[node]:
                    path = [(node, toNode)]
                    while self.isOneInOneOut(toNode):
                        self.visited[toNode] = True
                        toNodeNext = self.adjacencyList[toNode][0]
                        path.append((toNode, toNodeNext))
                        toNode = toNodeNext
                    paths.append(path)
        
        for node in self.adjacencyList.keys():
            path = []
            while  self.isOneInOneOut(node) and node not in self.visited:
                self.visited[node] = True
                toNode = self.adjacencyList[node][0]
                path.append((node, toNode))
                node = toNode
            if path:
                paths.append(path)
        
        return paths


for line in DBGraph(lines).findNonBranchingPaths():
    #print " -> ".join([line[0][0], line[0][1]] + [i[1] for i in line[1:]])
    contigs = [line[0][0], line[0][1]] + [i[1] for i in line[1:]]
    print contigs[0] + "".join([l[-1] for l in contigs[1:]]), 



