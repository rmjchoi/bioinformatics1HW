__author__ = 'Mauricio'
from classes import sequence

#Main
sequence1 = sequence("GCATGCUT")
sequence2 = sequence("GATTACA")

match = 1
gap = -1
mismatch = -2

colLen = sequence1.get_length()
rowLen = sequence2.get_length()
colChar = sequence1.get_sequence()
rowChar = sequence2.get_sequence()

#We initialize the matrix that will hold the scores
matrix = [[0 for i in range(colLen + 1)] for j in range(rowLen + 1)]


#Create recursive function for matrix initialization with gap values on the first x and y row
#Recursive format
def initMatrix(seq1, seq2, r, c):
    # if c==0 and r==0:
    #     matrix[r][c]=0
    #     initMatrix(seq1,seq2,r,c+1)
    #     initMatrix(seq1,seq2,r+1,c)
    #
    # elif c < colLen+1 and r == 0:
    #     matrix[r][c] = matrix[r][c-1]+gap
    #     c=c+1
    #     initMatrix(seq1,seq2,r,c)
    #
    # elif r < rowLen+1 and c == 0:
    #     matrix[r][c] = matrix [r-1][c]+gap
    #     r = r+1
    #     initMatrix(seq1,seq2,r,c)

# Initialize matrix w/o recursive
    matrix[0][0] = 0

    for c in range(1,colLen+1):
            matrix[r][c] = matrix[r][c-1]+gap

    for r in range(1,rowLen+1):
            matrix[r][0] = matrix[r-1][0]+gap
initMatrix(colChar,rowChar,0,0)

#Call matrix scoring recursive function

#Create recursive function for matrix scoring
def calculateMatrix (seq1, seq2, r, c):
    scoreMax = 0
    for s in sequence1:
        print s
    for c in range(1,colLen+1):
        for r in range(1,rowLen+1):
            if colChar == rowChar:
                scoreMax = match
            elif colChar != rowChar:
                scoreMax = mismatch

calculateMatrix(colChar,rowChar,0,0)



    #Call backtracking function
    # backwards(seq1, seq2, x, y)






#Create function for backtracking
def backwards(seq1, seq2, x, y):
    return


#print scoring matrix
for row in matrix:
    print row

#Print optimal alignment
