import csv
import numpy


class TriangleFinderSwapped:

    def __init__(self):
        with open('input.txt', 'rt') as textfile:
            self.input = textfile.read().splitlines()
            self.input = [[value for value in line.strip().split(' ') if value is not ''] for line in self.input]

    def reshape_data(self):
        self.input = [[int(y) for y in x] for x in self.input]
        reshaped_input = numpy.transpose(self.input)
        reshaped_input = numpy.reshape(reshaped_input, (-1, 3))
        self.input = reshaped_input.tolist()

    def filter_valid_triangles(self):
        self.input = [sorted(x) for x in self.input]
        self.input = [x for x in self.input if x[0] + x[1] > x[2]]

    def main(self):
        self.reshape_data()
        self.filter_valid_triangles()
        print(len(self.input))

if __name__ == "__main__":
    puzzle = TriangleFinderSwapped()
    puzzle.main()
