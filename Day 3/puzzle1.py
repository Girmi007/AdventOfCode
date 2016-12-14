import csv


class TriangleFinder:

    def __init__(self):
        with open('input.txt', 'rt') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', skipinitialspace=True)
            self.input = list(reader)

    def filter_valid_triangles(self):
        self.input = list(map(lambda x: sorted([int(y) for y in str.split(x[0])]), self.input))
        self.input = list(filter(lambda x: x[0] + x[1] > x[2], self.input))

    def main(self):
        self.filter_valid_triangles()
        print(len(self.input))

if __name__ == "__main__":
    puzzle = TriangleFinder()
    puzzle.main()
