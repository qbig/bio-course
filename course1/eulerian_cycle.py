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
        self.adjacencyList = {}
        self.outDegree = {}
        self.visited = {}
        for l in adjacencyList:
            startNode, endNodes = [l.strip() for l in l.split("->")]
            self.adjacencyList[startNode] = endNodes.split(",")
            self.outDegree[startNode] = len(self.adjacencyList[startNode])

        #print "Out Degree: ",self.outDegree

    def printGraph(self):
        for key in self.adjacencyList:
            print key, "->", self.adjacencyList[key]

    def getNext(self, currentNode):
        for node in self.adjacencyList[currentNode]:
            if (currentNode, node) not in self.visited and self.outDegree[currentNode] > 0:
                self.visited[(currentNode, node)] = True
                self.outDegree[currentNode] -= 1
                return node
        
        return -1

    def findCycle(self, startNode, currentNode, resultArr):
        if currentNode == startNode:
            #print startNode, resultArr, self.outDegree
            return resultArr 

        node = self.getNext(currentNode)
        resultArr.append(node)
        return self.findCycle(startNode, node, resultArr)

    def getUnfinishedNode(self, nodes):
        for index, node in enumerate(nodes):
            if self.outDegree[node] > 0:
                return index

        return -1


    def findPath(self):
        currentNode = self.adjacencyList.keys()[0]
        node = self.getNext(currentNode)
        path = []

        path += self.findCycle(currentNode, node, [currentNode, node])
        #print "path", path
        while self.getUnfinishedNode(path) != -1:
            indexNextStartNode = self.getUnfinishedNode(path)
            if indexNextStartNode == 0:
                path = path[:-1]
            else:
                # rotate and exclude last node 
                path = path[indexNextStartNode:-1] + path[:indexNextStartNode]
            nextNode = self.getNext(path[0])
            path += self.findCycle(path[0], nextNode, [path[0], nextNode])
            #print "path", path
        return path

#print "->".join(DBGraph(lines).findPath())
for line in DBGraph(lines).findPath():
    print line



