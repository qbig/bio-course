import sys

lines = [l.strip() for l in sys.stdin.readlines()]
k, d = [int(i.strip()) for i in lines[0].split()]
lines = lines[1:]

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
        self.inDegree = {}
        self.visited = {}
        self.nodes = set()
        for l in adjacencyList:
            startNode, endNodes = [l.strip() for l in l.split("->")]
            
            if startNode not in self.adjacencyList:
                self.adjacencyList[startNode] = endNodes.split(",")
                self.outDegree[startNode] = len(self.adjacencyList[startNode])
            else :
                self.adjacencyList[startNode] += endNodes.split(",")
                self.outDegree[startNode] = len(self.adjacencyList[startNode])

            if startNode not in self.nodes:
                self.nodes.add(startNode)
            
            for node in endNodes.split(","):
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

        print "unbalanced", unbalanced
        for i in unbalanced:
            print i, " in:", self.inDegree[i], "out:", self.outDegree[i]
        print "Out Degree: ",self.outDegree 
        print "In Degree:  ",self.inDegree

        if  self.outDegree[unbalanced[0]] < self.inDegree[unbalanced[0]]:
            if unbalanced[0] in self.adjacencyList:
                self.adjacencyList[unbalanced[0]].append(unbalanced[1])
                self.outDegree[unbalanced[0]] += 1
            else:
                self.adjacencyList[unbalanced[0]] = [unbalanced[1]]
                self.outDegree[unbalanced[0]] = 1
            self.unbalanced = unbalanced
        else:
            if unbalanced[1] in self.adjacencyList:
                self.adjacencyList[unbalanced[1]].append(unbalanced[0])
                self.outDegree[unbalanced[1]] += 1
            else:
                self.adjacencyList[unbalanced[1]] = [unbalanced[0]]
                self.outDegree[unbalanced[1]] = 1
                
            self.unbalanced = [unbalanced[1], unbalanced[0]]

        print "Out Degree: ",self.outDegree 
        print "In Degree:  ",self.inDegree
        print self.unbalanced 
        self.printGraph()

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

        addedEdgeFrom, addedEdgeTo = 0, 0
        for i in range(len(path)):
            if path[i] == self.unbalanced[0] and path[i+1] == self.unbalanced[1]:
                addedEdgeFrom, addedEdgeTo = i, i+1
                break
        path = path[:-1]
        
        return path[addedEdgeTo:] + path[:addedEdgeTo]


print k, d
for line in DBGraph(lines).findPath():
    print line



