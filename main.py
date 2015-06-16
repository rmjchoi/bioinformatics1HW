__author__ = 'Mauricio'
from classes import sequence
from classes import matrix

#Main
sequence1 = sequence(seqA)
sequence2 = sequence(seqB)

matrix = matrix(sequence1.get_length(), sequence2.get_length(),1,-1,-1)

#We initialize the matrix that will hold the scores
#Create recursive function for matrix initialization with gap values on the first x and y row
#Recursive format
def initMatrix(seq1, seq2, r, c):
    if c==0 and r==0:
        matrix.set_position(r,c,0)
        #matrix[r][c]=0
        initMatrix(seq1,seq2,r,c+1)
        initMatrix(seq1,seq2,r+1,c)

    elif c < sequence1.get_length()+1 and r == 0:
        matrix.set_position(r,c,matrix.get_position(r,c-1) + matrix.get_gapscore())
       # matrix[r][c] = matrix[r][c-1]+ matrix.get_gapscore()
        c=c+1
        initMatrix(seq1,seq2,r,c)

    elif r < sequence2.get_length()+1 and c == 0:
        matrix.set_position(r,c,matrix.get_position(r-1,c) + matrix.get_gapscore())
        # matrix[r][c] = matrix [r-1][c]+gap
        r = r+1
        initMatrix(seq1,seq2,r,c)

    # Calculate
    elif r<=  sequence2.get_length()+1 and c <= sequence1.get_length()+1:
        calculateMatrix(seq1,seq2,0,0)

def calculateMatrix (seq1, seq2, r, c):
    if c < sequence1.get_length() :
        matrix.set_score(sequence1.get_char(c), sequence2.get_char(r), r, c)
        c = c + 1
        calculateMatrix(seq1, seq2, r, c)
    else:
        r= r+1
        if r < sequence2.get_length():
            calculateMatrix(seq1, seq2, r, 0)

# Initialize matrix w/o recursive
#     matrix[0][0] = 0
#
#     for c in range(1,colLen+1):
#             matrix[r][c] = matrix[r][c-1]+gap
#
#     for r in range(1,rowLen+1):
#             matrix[r][0] = matrix[r-1][0]+gap


#Call matrix scoring recursive function





    #Call backtracking function
    # backwards(seq1, seq2, x, y)






#Create function for backtracking
def backwards(seq1, seq2, x, y):
    return



initMatrix(sequence1.get_sequence(),sequence2.get_sequence(),0,0)



#print scoring matrix
matrix.print_matrix()

#Print optimal alignment
