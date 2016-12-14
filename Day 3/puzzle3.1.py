

class TriangleFinder:

    def __init__(self):
        with open('input.txt', 'rt') as textfile:
            self.input = textfile.read().splitlines()
            self.input = [[value for value in line.strip().split(' ') if value is not ''] for line in self.input]

    def filter_valid_triangles(self):
        self.input = list(map(lambda x: sorted([int(y) for y in x]), self.input))
        self.input = list(filter(lambda x: x[0] + x[1] > x[2], self.input))

    def main(self):
        self.filter_valid_triangles()
        print(len(self.input))

if __name__ == "__main__":
    puzzle = TriangleFinder()
    puzzle.main()
