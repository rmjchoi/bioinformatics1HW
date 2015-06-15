__author__ = 'Mauricio'
from classes import sequence

#Main
sequence1 = sequence("GCATGCU")
sequence2 = sequence("GATTACA")

#We initialize the matrix that will hold the scores
matrix = [[0 for i in range(sequence1.get_length() + 1)] for j in range(sequence2.get_length() + 1)]


#Create recursive function for matrix initialization with gap values on the first x and y row
def initMatrix(seq1, seq2, x, y):
    #Process

    #Call matrix scoring recursive function
    calculateMatrix(seq1, seq2, x, y)







#Create recursive function for matrix scoring
def calculateMatrix (seq1, seq2, x, y):
    #Process


    #Call backtracking function
    backwards(seq1, seq2, x, y)





#Create function for backtracking
def backwards(seq1, seq2, x, y):
    return


#print scoring matrix
for row in matrix:
    print row

#Print optimal alignment
