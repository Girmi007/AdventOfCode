import numpy as np
import string
from operator import itemgetter


class Unjammer:

    def __init__(self):
        with open('input.txt', 'rt') as textfile:
            self.input = textfile.read().splitlines()

    def unjam(self):
        input_matrix = np.matrix([list(line) for line in self.input]).transpose().tolist()
        column_letter_counts = [[[row.count(letter), letter] for letter in string.ascii_lowercase]
                                for row in input_matrix]
        top_letters = [sorted(column_letter_count, reverse=True, key=itemgetter(0))[0]
                       for column_letter_count in column_letter_counts]
        print("Message: %s" % ''.join(x[1] for x in top_letters))

    def main(self):
        self.unjam()

if __name__ == "__main__":
    puzzle = Unjammer()
    puzzle.main()
