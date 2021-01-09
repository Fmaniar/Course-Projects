import random
import math
class Board():

    def __init__(self, numRowsCols):
        self.cells = [[0] * numRowsCols for i in range(numRowsCols)]
        self.numRows = numRowsCols
        self.numCols = numRowsCols

		# negative value for initial h...easy to check if it's been set or not
        self.h = -1

    # Print board
    def printBoard(self):
        for row in self.cells:
            print (row)

    # Randomize the board
    def rand(self):
        self.cells = [[0] * self.numRows for i in range(self.numRows)]
        for row in self.cells:
            i = random.randint(0, self.numCols-1)
            row[i] = 1

    # Swap two locations on the board
    def swapLocs(self, a, b):
        temp = self.cells[a[0]][a[1]]
        self.cells[a[0]][a[1]] = self.cells[b[0]][b[1]]
        self.cells[b[0]][b[1]] = temp





# Cost function for a board
def numAttackingQueens(board):

    # Collect locations of all queens
    locs = []
    for r in range( len(board.cells) ):
        for c in range( len(board.cells[r]) ):
            if board.cells[r][c] == 1:
                locs.append([r, c])
    #print 'Queen locations: %s' % locs

    result = 0

    # For each queen (use the location for ease)
    for q in locs:

        # Get the list of the other queen locations
        others = [x for x in locs if x != q]
        #print 'q: %s others: %s' % (q, others)
    
        count = 0
        # For each other queen
        for o in others:
            #print 'o: %s' % o
            diff = [o[0] - q[0], o[1] - q[1]]

            # Check if queens are attacking
            if o[0] == q[0] or o[1] == q[1] or abs(diff[0]) == abs(diff[1]):
                count = count + 1

        # Add the amount for this queen
        result = result + count

    return result




# Move any queen to another square in the same column
# successors all the same                                                                                    
def getSuccessorStates(board):
    result = []

    for i_row, row in enumerate(board.cells):
        # Get the column the queen is on in this row
        # [0] because list comprehension returns a list, even if only one element
        # This line will crash if the board has not been initialized with rand() or some other method
        i_queen = [i for i,x in enumerate(row) if x == 1][0]

        # For each column in the row
        for i_col in range(board.numCols):

            # If the queen is not there
            if row[i_col] != 1:
                # Make a copy of the board
                bTemp = Board(board.numRows)
                bTemp.cells[:] = [r[:] for r in board.cells]

                # Now swap queen to i_col from i_queen
                bTemp.swapLocs([i_row, i_col], [i_row, i_queen])
                #bTemp.printBoard()
                result.append(bTemp)

    return result

def schedule(T, decayRate):
    return(T*decayRate)
def simAnnel(decayRate, termVal, boardSize):
    print("**********************************")
    print("Board side: " + str(boardSize))
    print("**********************************")
    finalavgH = 0
    print("######################################")
    print("decay rate: " + str(decayRate) + " T threshold: " + str(termVal))
    print("######################################")
    for t in range(0,10):
        T = 100
        b = Board(boardSize)
        b.rand()
        print("run: " + str(t))
        print("initial board")
        b.printBoard()
        print("h value: ")
        print(numAttackingQueens(b))
        T = schedule(T, decayRate)
        while(T > termVal and (numAttackingQueens(b) > 0)):
            T = schedule(T, decayRate)
            nextB = random.choice(getSuccessorStates(b))
            delE = numAttackingQueens(b) - numAttackingQueens(nextB)
            if (delE > 0):
                b = nextB
            elif (math.e**(delE/T) > random.uniform(0,1)):
                b = nextB
        print("final board h value: ")
        print(numAttackingQueens(b))
        finalavgH = finalavgH + numAttackingQueens(b)
        b.printBoard()
    print("Average h-cost of final solutions: " + str(finalavgH/10))
    



def main():
    simAnnel(.9, 0.000001, 4)
    simAnnel(.75, 0.0000001, 4)
    simAnnel(.5, 0.00000001, 4)
    simAnnel(.9, 0.000001, 8)
    simAnnel(.75, 0.0000001, 8)
    simAnnel(.5, 0.00000001, 8)
    simAnnel(.9, 0.000001, 16)
    simAnnel(.75, 0.0000001, 16)
    simAnnel(.5, 0.00000001, 16)
main()