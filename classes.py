__author__ = 'Mauricio'
import math
class sequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def get_sequence(self):
        return self.sequence

    def get_length(self):
        return len(self.sequence)

    def get_char(self,x):
        return self.sequence[x]
    # def get_char(self):
    #     return self.


    def set_sequence(self, seq):
        self.sequence = seq

    def add_char(self, char):
        newseq = char + self.get_sequence()
        self.set_sequence(newseq)

class matrix:
    def __init__(self, width, height):
        self.matrix = [[0 for i in range(width + 1)] for j in range(height + 1)]
        self.matchscore = 1
        self.mismatchscore = 0
        self.gapscore = -1
        self.gapstartscore = -2
        self.use_score = 0
        self.gapstartscore_flag = "N"

    def get_position(self, x, y):
        return self.matrix[x][y]

    def set_position(self,x,y,value):
        self.matrix[x][y] = value

    def print_matrix(self):
        for row in self.matrix:
            print row

    def set_score(self,a,b,x,y):
        if self.use_score == 1:
            if a == b: #if it the characters match
                #Get the highest score according to the highest position
                if (self.matrix[x][y] + self.matchscore) >= (self.matrix[x][y + 1] + self.gapscore) and (self.matrix[x][y] + self.matchscore) >= (self.matrix[x+1][y] + self.gapscore):
                    self.matrix[x+1][y+1] = self.matrix[x][y] + self.matchscore
                if (self.matrix[x+1][y] + self.gapscore) >= (self.matrix[x][y + 1] + self.gapscore) and (self.matrix[x+1][y] + self.gapscore) >= (self.matrix[x][y] + self.matchscore):
                    self.matrix[x+1][y+1] = self.matrix[x+1][y] + self.gapscore
                if (self.matrix[x][y+1] + self.gapscore) >= (self.matrix[x][y] + self.matchscore) and (self.matrix[x][y+1] + self.gapscore) >= (self.matrix[x+1][y] + self.gapscore):
                    self.matrix[x+1][y+1] = self.matrix[x][y+1] + self.gapscore

            #If letter A and letter B are a mismatch:
            elif a != b:
                #Get the highest score according to the highest position

                if (self.matrix[x][y] + self.mismatchscore) >= (self.matrix[x][y + 1] + self.gapscore) and (self.matrix[x][y] + self.mismatchscore) >= (self.matrix[x+1][y] + self.gapscore):
                    self.matrix[x+1][y+1] = self.matrix[x][y] + self.mismatchscore
                if (self.matrix[x+1][y] + self.gapscore) >= (self.matrix[x][y + 1] + self.gapscore) and (self.matrix[x+1][y] + self.gapscore) >= (self.matrix[x][y] + self.mismatchscore):
                    self.matrix[x+1][y+1] = self.matrix[x+1][y] + self.gapscore
                if (self.matrix[x][y+1] + self.gapscore) >= (self.matrix[x][y] + self.mismatchscore) and (self.matrix[x][y+1] + self.gapscore) >= (self.matrix[x+1][y] + self.gapscore):
                    self.matrix[x+1][y+1] = self.matrix[x][y+1] + self.gapscore


        if self.use_score == 2:
            if a == b: #if it the characters match
                #Get the highest score according to the highest position
                if (self.matrix[x][y] + self.matchscore) >= (self.matrix[x][y + 1] + self.gapstartscore) and (self.matrix[x][y] + self.matchscore) >= (self.matrix[x+1][y] + self.gapstartscore):
                    self.matrix[x+1][y+1] = self.matrix[x][y] + self.matchscore
                    self.gapstartscore_flag = "N"
                if (self.matrix[x+1][y] + self.gapstartscore) >= (self.matrix[x][y + 1] + self.gapstartscore) and (self.matrix[x+1][y] + self.gapstartscore) >= (self.matrix[x][y] + self.matchscore):
                    if self.gapstartscore_flag == "T":
                        self.matrix[x+1][y+1] = self.matrix[x+1][y] + self.gapscore
                    else:
                        self.matrix[x+1][y+1] = self.matrix[x+1][y] + self.gapstartscore
                        self.gapstartscore_flag = "T"
                if (self.matrix[x][y+1] + self.gapstartscore) >= (self.matrix[x][y] + self.matchscore) and (self.matrix[x][y+1] + self.gapstartscore) >= (self.matrix[x+1][y] + self.gapstartscore):
                    if self.gapstartscore_flag == "L":
                        self.matrix[x+1][y+1] = self.matrix[x][y+1] + self.gapscore
                    else:
                        self.matrix[x+1][y+1] = self.matrix[x][y+1] + self.gapstartscore
                        self.gapstartscore_flag = "L"

            #If letter A and letter B are a mismatch:
            elif a != b:
                #Get the highest score according to the highest position

                if (self.matrix[x][y] + self.mismatchscore) >= (self.matrix[x][y + 1] + self.gapstartscore) and (self.matrix[x][y] + self.mismatchscore) >= (self.matrix[x+1][y] + self.gapstartscore):
                    self.matrix[x+1][y+1] = self.matrix[x][y] + self.mismatchscore
                    self.gapstartscore_flag = "N"
                if (self.matrix[x+1][y] + self.gapstartscore) >= (self.matrix[x][y + 1] + self.gapstartscore) and (self.matrix[x+1][y] + self.gapstartscore) >= (self.matrix[x][y] + self.mismatchscore):
                    if self.gapstartscore_flag == "T":
                        self.matrix[x+1][y+1] = self.matrix[x+1][y] + self.gapscore
                    else:
                        self.matrix[x+1][y+1] = self.matrix[x+1][y] + self.gapstartscore
                        self.gapstartscore_flag = "T"
                if (self.matrix[x][y+1] + self.gapstartscore) >= (self.matrix[x][y] + self.mismatchscore) and (self.matrix[x][y+1] + self.gapstartscore) >= (self.matrix[x+1][y] + self.gapstartscore):
                    if self.gapstartscore_flag == "L":
                        self.matrix[x+1][y+1] = self.matrix[x][y+1] + self.gapscore
                    else:
                        self.matrix[x+1][y+1] = self.matrix[x][y+1] + self.gapstartscore
                        self.gapstartscore_flag = "L"

        if self.use_score == 3:
            self.matrix[0][y+1] and self.matrix[x+1][0]

            if a == b :
                if (self.matrix[x][y]+self.matchscore) >= (self.matrix[x][y+1]+self.mismatchscore) and (self.matrix[x][y]+self.matchscore) >= (self.matrix[x+1][y]+self.mismatchscore)\
                        and (self.matrix[x][y]+self.matchscore) >= 0:
                    self.matrix[x+1][y+1] = self.matrix[x][y] + self.matchscore
                if (self.matrix[x+1][y]+self.mismatchscore) >= (self.matrix[x][y+1]+self.mismatchscore) and (self.matrix[x+1][y]+self.mismatchscore) >= (self.matrix[x][y]+self.matchscore)\
                        and (self.matrix[x+1][y]+self.mismatchscore) >= 0:
                    self.matrix[x+1][y+1] = self.matrix[x+1][y] + self.mismatchscore
                if(self.matrix[x][y+1]+self.mismatchscore) >= (self.matrix[x+1][y]+self.mismatchscore) and (self.matrix[x][y+1]+self.mismatchscore) >= (self.matrix[x][y]+self.matchscore)\
                        and (self.matrix[x][y+1]+self.mismatchscore) >= 0:
                    self.matrix[x+1][y+1] = self.matrix[x][y+1] + self.gapscore
                if(self.matrix[x][y]+self.matchscore) <= 0 and (self.matrix[x+1][y]) <= 0 and (self.matrix[x][y+1] <= 0):
                    self.matrix[x+1][y+1] = 0

            if a != b :
                if (self.matrix[x][y]+self.mismatchscore) >= (self.matrix[x][y+1]+self.mismatchscore) and (self.matrix[x][y]+self.mismatchscore) >= (self.matrix[x+1][y]+self.mismatchscore)\
                        and (self.matrix[x][y]+self.mismatchscore) >= 0:
                    self.matrix[x+1][y+1] = self.matrix[x][y] + self.mismatchscore
                if (self.matrix[x+1][y]+self.mismatchscore) >= (self.matrix[x][y+1]+self.mismatchscore) and (self.matrix[x+1][y]+self.mismatchscore) >= (self.matrix[x][y]+self.mismatchscore)\
                        and (self.matrix[x+1][y]+self.matchscore) >= 0:
                    self.matrix[x+1][y+1] = self.matrix[x+1][y] +self.mismatchscore
                if(self.matrix[x][y+1]+self.mismatchscore) >= (self.matrix[x+1][y]+self.mismatchscore) and (self.matrix[x][y+1]+self.mismatchscore) >= (self.matrix[x][y]+self.matchscore)\
                        and (self.matrix[x][y+1]+self.mismatchscore) >= 0:
                    self.matrix[x+1][y+1] = self.matrix[x][y+1] + self.matchscore
                if(self.matrix[x][y]+self.matchscore) <= 0 and (self.matrix[x+1][y]) <= 0 and (self.matrix[x][y+1]) <= 0:
                    self.matrix[x+1][y+1] = 0


            # if a == b :
            #     if(self.matrix[x][y] + self.)
            #
            # elif a != b :


    def get_matchscore(self):
        return self.matchscore

    def set_matchscore(self,score):
        self.matchscore = score

    def get_mismatchscore(self):
        return self.mismatchscore

    def set_mismatchscore(self,score):
        self.mismatchscore = score

    def get_gapscore(self):
        return self.gapscore

    def set_gapscore(self,score):
        self.gapscore = score

    def get_gapstartscore(self):
        return self.gapstartscore

    def set_gapstartscore(self,score):
        self.gapstartscore = score

    def set_usegapscore(self, boolean):
        self.use_gapstartscore = boolean

    def backtracking(self, seq1, seq2, x, y, align1, align2):
        #Backtracking function
        #While the x and y coordinates dont reach zero, will compare the 3 possible ways for the alignment to happend
        if self.use_score == 1 or self.use_score == 2:
            if x > 0 or y > 0:
                if self.matrix[x-1][y-1] >= self.matrix[x][y-1] and self.matrix[x-1][y-1] >= self.matrix[x-1][y]:
                    align1 = seq1[y-1] + align1
                    align2 = seq2[x-1] + align2
                    return self.backtracking(seq1, seq2, x-1, y-1, align1, align2)
                elif self.matrix[x-1][y] >= self.matrix[x][y-1] and self.matrix[x-1][y] >= self.matrix[x][y]:
                    align1 = "-" + align1
                    align2 = seq2[x-1] + align2
                    return self.backtracking(seq1, seq2, x-1, y, align1, align2)
                elif self.matrix[x][y-1] >= self.matrix[x][y] and self.matrix[x][y-1] >= self.matrix[x-1][y]:
                    align1 = seq1[y-1] + align1
                    align2 = "-" + align2
                    return self.backtracking(seq1, seq2, x, y-1, align1, align2)
            else:
                return align1, align2

        # elif self.use_score == 3 :
