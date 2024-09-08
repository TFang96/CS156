import math


def main():
    adjacencyMatrix = CreateAdjacencyMatrix()
    distances = BFAlgorithmDist(adjacencyMatrix)
    vertexData = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}
    for i in range(1, 7):
        print("Shortest distance to " + str(vertexData[i]) + "is: " + str(distances[i]))

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


def BFAlgorithmDist(Matrix):
    D = []
    D.append(0)
    for i in range(1, 7):
        D.append(Matrix[0][i])
    for i in range(6):
        for j in range (7):
            for k in range(1, 7):
                if Matrix[0][j] + Matrix[j][k] < D[k]:
                    D[k] = Matrix[0][j] + Matrix[j][k]
    return D


main()

