import math


def main():
    adjacencyMatrix = CreateAdjacencyMatrix()
    pathData = BFAlgorithm(adjacencyMatrix)
    if not pathData:
        print("Error, there exists a negative cycle. ")
    else:
        print("No negative cycle exists. ")
        vertexData = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}
        for i in range(1, 7):
            print("Shortest distance to " + str(vertexData[i]) + " is: " + str(pathData[0][i]))
        for i in range(1, 7):
            print("Path to " + str(vertexData[i]) + " is: " + str(pathData[1][i]))


def CreateAdjacencyMatrix():
    size = 7
    adjacencyMatrix = []
    for i in range(size):
        adjacencyMatrix.append([])
        for j in range(size):
            adjacencyMatrix[i].append([])
    for i in range(size):
        for j in range(size):
            adjacencyMatrix[i][j] = math.inf
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
    for i in range(7):
        adjacencyMatrix[i][i] = 0

    return adjacencyMatrix


def BFAlgorithm(Matrix):
    returnData = []
    vertexData = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}
    D = []
    P = []
    for i in range(7):
        P.append([])
    for i in range(1, 7):
        if Matrix[0][i] != math.inf:
            P[i].append(vertexData[i])
    D.append(0)
    for i in range(1, 7):
        D.append(Matrix[0][i])
    for i in range(7):
        for j in range(7):
            for k in range(7):
                if D[j] + Matrix[j][k] < D[k]:
                    D[k] = D[j] + Matrix[j][k]
                    if len(P[k]) != 0:
                        P[k] = []
                    if len(P[j]) != 0:
                        for prev in range(len(P[j])):
                            P[k].append(P[j][prev])
                        P[k].append(vertexData[k])
                    else:
                        P[k].append(vertexData[j])
                        P[k].append(vertexData[k])

    for i in range(7):
        for j in range(7):
            if D[i] + Matrix[i][j] < D[j]:
                return False

    returnData.append(D)
    returnData.append(P)
    return returnData


main()
