#Homework 1 - CS156
#Written By: Ziheng (Tony) Fang and Ashwabh Bhatnagar


import math


def main():
    adjacencyMatrix = CreateAdjacencyMatrix() # this is the adjacency matrix
    pathData = BFAlgorithm(adjacencyMatrix) # this is the paths to each node from 's'
    '''This checks to see if a negative cycle exists'''
    if not pathData:
        print("Error, there exists a negative cycle. ")
    else:
        print("No negative cycle exists. ")
        '''This translates the index into the corresponding vertex.'''
        vertexData = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}
        '''This prints out the shortest distance to each vertex.'''
        for i in range(1, 7):
            print("Shortest distance to " + str(vertexData[i]) + " is: " + str(pathData[0][i]))
        '''This prints out the path data to each vertex.'''
        for i in range(1, 7):
            print("Path to " + str(vertexData[i]) + " is: " + str(pathData[1][i]))


def CreateAdjacencyMatrix():
    size = 7 #size is hardcoded
    adjacencyMatrix = []
    for i in range(size):
        adjacencyMatrix.append([])
        for j in range(size):
            adjacencyMatrix[i].append([])
    '''Start with all infinity. '''
    for i in range(size):
        for j in range(size):
            adjacencyMatrix[i][j] = math.inf
    '''We then add edge data. '''
    adjacencyMatrix[0][1] = 6
    adjacencyMatrix[0][2] = 5
    adjacencyMatrix[0][3] = 5
    adjacencyMatrix[1][4] = -1
    adjacencyMatrix[2][1] = -2
    adjacencyMatrix[2][4] = 1
    adjacencyMatrix[3][2] = -2
    adjacencyMatrix[3][5] = -1
    adjacencyMatrix[4][6] = 3
    adjacencyMatrix[5][6] = 3
    '''Going from a node to itself should not cost anything...'''
    for i in range(7):
        adjacencyMatrix[i][i] = 0

    return adjacencyMatrix


def BFAlgorithm(Matrix):
    returnData = [] # will contain data we return.
    vertexData = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}
    D = [] # contains distances to each vertex.
    P = [] # contains detailed paths to each vertex
    for i in range(7):
        P.append([])
    for i in range(1, 7):
        if Matrix[0][i] != math.inf:
            P[i].append(vertexData[i])
    D.append(0) #going from start to itself will not cost anything
    for i in range(1, 7):
        D.append(Matrix[0][i])
    '''Loop through the graph V-1 times.'''
    for i in range(len(Matrix)-1):
        for j in range(len(Matrix)):
            for k in range(len(Matrix)):
                '''If we find a shorter path, we relax. '''
                if D[j] + Matrix[j][k] < D[k]:
                    D[k] = D[j] + Matrix[j][k]
                    '''Update path data from start to new node. '''
                    if len(P[k]) != 0:
                        P[k] = []
                    if len(P[j]) != 0:
                        for prev in range(len(P[j])):
                            P[k].append(P[j][prev])
                        P[k].append(vertexData[k])
                    else:
                        P[k].append(vertexData[j])
                        P[k].append(vertexData[k])
    '''This checks for any negative cycles. '''
    for i in range(len(Matrix)):
        for j in range(len(Matrix)):
            if D[i] + Matrix[i][j] < D[j]:
                return False
    for i in range(len(P)):
        P[i].insert(0, 's')
    returnData.append(D)
    returnData.append(P)
    return returnData


main()
