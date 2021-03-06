__author__ = 'Mauricio'

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

    def get_maxIndex(self, seq1, seq2):
        max = 0
        # indexR = 0 indexC = 0
        # Searching for the maximum value and it's position
        x, y = len(seq1), len(seq2)
        for j in range(x+1):
             for i in range(y+1):
                if max < self.matrix[i][j]:
                    indexR,indexC  = i,j
                    max = self.matrix[i][j]
        return indexR,indexC

    def get_scoresystem(self):
        return self.use_score

    def set_score(self,a,b,x,y):
        score = 0;
        #Checks if the characters are a match or not, and assign the value to score, so we can use during the scoring system
        if a == b: #if it the characters match
            score = self.matchscore
        else:
            score = self.mismatchscore

        #Normal scoring system
        if self.use_score == 1:
            #Get the highest score according to the highest position
            if (self.matrix[x][y] + score) >= (self.matrix[x][y + 1] + self.gapscore) and (self.matrix[x][y] + score) >= (self.matrix[x+1][y] + self.gapscore):
                self.matrix[x+1][y+1] = self.matrix[x][y] + score
            if (self.matrix[x+1][y] + self.gapscore) >= (self.matrix[x][y + 1] + self.gapscore) and (self.matrix[x+1][y] + self.gapscore) >= (self.matrix[x][y] + score):
                self.matrix[x+1][y+1] = self.matrix[x+1][y] + self.gapscore
            if (self.matrix[x][y+1] + self.gapscore) >= (self.matrix[x][y] + score) and (self.matrix[x][y+1] + self.gapscore) >= (self.matrix[x+1][y] + self.gapscore):
                self.matrix[x+1][y+1] = self.matrix[x][y+1] + self.gapscore

        #Gap penalty scoring system
        if self.use_score == 2:
        #We keep track of the last gap on the gapstartscore_flag variable
            #Get the highest score according to the highest position
            if (self.matrix[x][y] + score) >= (self.matrix[x][y + 1] + self.gapstartscore) and (self.matrix[x][y] + score) >= (self.matrix[x+1][y] + self.gapstartscore):
                self.matrix[x+1][y+1] = self.matrix[x][y] + score
                self.gapstartscore_flag = "N"
            if (self.matrix[x+1][y] + self.gapstartscore) >= (self.matrix[x][y + 1] + self.gapstartscore) and (self.matrix[x+1][y] + self.gapstartscore) >= (self.matrix[x][y] + score):
                if self.gapstartscore_flag == "T":
                    self.matrix[x+1][y+1] = self.matrix[x+1][y] + self.gapscore
                else:
                    self.matrix[x+1][y+1] = self.matrix[x+1][y] + self.gapstartscore
                    self.gapstartscore_flag = "T"
            if (self.matrix[x][y+1] + self.gapstartscore) >= (self.matrix[x][y] + score) and (self.matrix[x][y+1] + self.gapstartscore) >= (self.matrix[x+1][y] + self.gapstartscore):
                if self.gapstartscore_flag == "L":
                    self.matrix[x+1][y+1] = self.matrix[x][y+1] + self.gapscore
                else:
                    self.matrix[x+1][y+1] = self.matrix[x][y+1] + self.gapstartscore
                    self.gapstartscore_flag = "L"

        #Local alignment scoring, if there is a negative score, convert to zero
        if self.use_score == 3:
            if (self.matrix[x][y] + score) >= (self.matrix[x][y + 1] + self.gapscore) and (self.matrix[x][y] + score) >= (self.matrix[x+1][y] + self.gapscore):
                if (self.matrix[x][y] + score) >= 0:
                    self.matrix[x+1][y+1] = self.matrix[x][y] + score
                else :
                    self.matrix[x+1][y+1] = 0
            if (self.matrix[x+1][y] + self.gapscore) >= (self.matrix[x][y + 1] + self.gapscore) and (self.matrix[x+1][y] + self.gapscore) >= (self.matrix[x][y] + score):
                if (self.matrix[x+1][y] + self.gapscore) >= 0:
                    self.matrix[x+1][y+1] = self.matrix[x+1][y] + self.gapscore
                else :
                    self.matrix[x+1][y+1] = 0
            if (self.matrix[x][y+1] + self.gapscore) >= (self.matrix[x][y] + score) and (self.matrix[x][y+1] + self.gapscore) >= (self.matrix[x+1][y] + self.gapscore):
                if (self.matrix[x][y+1] + self.gapscore) >= 0:
                    self.matrix[x+1][y+1] = self.matrix[x][y+1] + self.gapscore
                else :
                    self.matrix[x+1][y+1] = 0


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

    def set_scoresystem(self,number):
        self.use_score = number

    def set_gapstartscore(self,score):
        self.gapstartscore = score

    def set_usegapscore(self, boolean):
        self.use_gapstartscore = boolean

    def backtracking(self, seq1, seq2, x, y, align1, align2):
        #Backtracking function
        #While the x and y coordinates dont reach zero, will compare the 3 possible ways for the alignment to happend

        #Same backtracking for basic score and gap scoring system
        if self.use_score == 1 or self.use_score == 2:
            if x > 0 or y > 0:
                 #  walk towards the highest score
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

        #Backtracking for local scoring scheme
        if self.use_score == 3:
            spaces = ""
            if self.matrix[x][y] == 0:
                c,r = self.get_maxIndex(seq1,seq2)
                #We calculate the spaces needed for visual alignment
                if len (seq1[:y]) > len(seq2[:x]):
                    spaces = " " * len (seq1[:y])
                    return seq1[:y] + align1 + seq1[r:], spaces + seq2[:x] + align2 + seq2[c:]
                elif len (seq1[:y]) <  len(seq2[:x]):
                    spaces = " " * len (seq2[:x])
                    return spaces+ seq1[:y] + align1 + seq1[r:],seq2[:x] + align2 + seq2[c:]
                else:
                    return seq1[:y] + align1 + seq1[r:], seq2[:x] + align2 + seq2[c:]
            #  walk towards the highest score
            elif x > 0 or y > 0:
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
            # either side






