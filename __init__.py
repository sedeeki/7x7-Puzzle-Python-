import random
import gurobipy as gp


def checkColumn(matrix, colNum):      #Checks the whole column if that column already had a grid value chosen
    for i in range(7):
        if (matrix[i][colNum] == -1):
            return False
    return True

def checkRow(matrix,row):    #Checks the whole row if that row already had a grid value chosen
    for i in range(7):
        if (matrix[row][i] == -1):
            return False
    return True

def getMax(matrix):    #Gets the max value from the 7x7 Square and returns its row and col index
    gotValue = False   # The max value is checked row wise and col wise.. if conditions are not met,
    while (gotValue == False):                 # the function starts finding the next biggest number
        maxVal = 0
        colNum = -1
        rowNum = -1
        for i in range(7):
            for j in range(7):
                if (maxVal < matrix[i][j]):
                    maxVal = matrix[i][j]
                    colNum = j
                    rowNum = i
        if (checkColumn(matrix,colNum) == True and checkRow(matrix,rowNum) == True):
            gotValue = True
        else:
            matrix[rowNum][colNum] = 0
    return rowNum, colNum

def getMaxOnGrid(matrix,total,iterations):      #recursive function 
    if (iterations == 7):      #breaks when all 7 values have been selected
        return matrix, total
    
    rowNum, colNum = getMax(matrix)
    value = matrix[rowNum][colNum]
    total = total + value
    matrix[rowNum][colNum] = -1      # changes the selected grid value to -1 and appends in total
    return getMaxOnGrid(matrix, total, iterations + 1)    
        

def solveGridProblem(matrix):
    print("Original Matrix: ")
    for i in matrix:
        print(i)
    print(" ")
    newMatrix, totalSum = getMaxOnGrid(matrix, 0, 0)
    matrix = [[5,4,6,7,1,5,6],                # Original matrix
         [9,8,5,1,1,2,3],
         [1,7,4,6,2,3,5],
         [1,1,2,4,2,6,2],
         [15,12,1,3,10,8,2],
         [16,17,1,1,6,6,2],
         [3,5,8,1,2,1,1]]
    for i in range(7):
        for j in range(7):
            if (newMatrix[i][j] != -1):
                newMatrix[i][j] = matrix[i][j]     # New Matrix
    print("The Matrix with values selected and replaced with -1")
    for i in newMatrix:
        print(i)
    print("Total Sum: ", totalSum) 

if __name__ == '__main__':
    try:
        matrix = [[5,4,6,7,1,5,6],
         [9,8,5,1,1,2,3],
         [1,7,4,6,2,3,5],
         [1,1,2,4,2,6,2],
         [15,12,1,3,10,8,2],
         [16,17,1,1,6,6,2],
         [3,5,8,1,2,1,1]]
        solveGridProblem(matrix)
    
    except gp.GurobiError as e:
        print("Error Code:" + str(e.errno))
    
    