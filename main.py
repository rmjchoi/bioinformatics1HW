__author__ = 'Mauricio'
from classes import sequence
from classes import matrix


#Initialize matrix w/o recursive, only the first column and row are filled with the acumulated gap score
def startAligning(seq1, seq2, r, c):
    matrix.set_position(0,0,0)
    for c in range(1,sequence1.get_length()+1):
        matrix.set_position(r,c,matrix.get_position(r,c-1) + matrix.get_gapscore())
    for r in range(1,sequence2.get_length()+1):
        matrix.set_position(r,0,matrix.get_position(r-1,0) + matrix.get_gapscore())
    calculateMatrix(seq1,seq2,0,0)


#Recursive function, we calculate the entire matrix, using the function set_score from the matrix class
def calculateMatrix (seq1, seq2, r, c):
    global align1
    global align2
    #For every character on the first sequence, compare against a character of the second sequence
    if c < sequence1.get_length() :
        matrix.set_score(sequence1.get_char(c), sequence2.get_char(r), r, c)
        c = c + 1
        calculateMatrix(seq1, seq2, r, c)
    else:
        r= r+1
        #Once we are done comparing with a character of the second sequence, we jump to the next one and repeat
        if r < sequence2.get_length():
            calculateMatrix(seq1, seq2, r, 0)
        else:
            #We call the function backtracking from the matrix class. Recursive function.
            align1, align2 = matrix.backtracking(seq1 ,seq2 ,r ,c, "", "" )

#Main
sequence1 = sequence(raw_input("Insert sequence1"))
sequence2 = sequence(raw_input("Insert sequence2"))


#Variables where the aligned sequences will be stored
align1 = ""
align2 = ""

#We create the matrix according to the length of the two sequences, and giving the scores that will be used for the scoring, match, mismatch and gap
matrix = matrix(sequence1.get_length(), sequence2.get_length(),1,-1,-1)
#We initialize the process, givng the two sequences, and initial coordinates for the matrix
startAligning(sequence1.get_sequence(),sequence2.get_sequence(),0,0)

#print information
matrix.print_matrix()
print"############Sequences#############"
print sequence1.get_sequence()
print sequence2.get_sequence()
print"############Alignment#############"
print align1
print align2
print"##################################"

