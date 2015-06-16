__author__ = 'Mauricio'

class sequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def get_sequence(self):
        return self.sequence

    def get_length(self):
        return len(self.sequence)

    def set_sequence(self, seq):
        self.sequence = seq

    def add_char(self, char):
        newseq = char + self.get_sequence()
        self.set_sequence(newseq)

class matrix:
    def __init__(self, width, height, match, mismatch, gap):
        self.matrix = [[0 for i in range(width + 1)] for j in range(height + 1)]
        self.matchscore = match
        self.mismatchscore = mismatch
        self.gapscore = gap

    def get_position(self, x, y):
        return self.matrix[x][y]

    def set_position(self,x,y,value):
        self.matrix[x][y] = value

    def print_matrix(self):
        for row in self.matrix:
            print row

    def set_score(self,a,b,x,y):
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

    def get_matchscore(self):
        return self.matchscore

    def get_mismatchscore(self):
        return self.mismatchscore

    def get_gapscore(self):
        return self.gapscore