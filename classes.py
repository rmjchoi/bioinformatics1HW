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