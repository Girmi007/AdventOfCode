import os
import csv


class ChecksumSolver:

    def __init__(self):

        input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
        with open(input_file_path, 'rt') as csvfile:
            reader = csv.reader(csvfile, skipinitialspace=True)
            self.instructions = list(reader)

    def main(self):
        # row_checksums = [(max(row)-min(row))for row in self.instructions]
        checksum = 0
        for row in self.instructions:
            row_ints = [int(nr) for nr in row[0].split()]
            checksum += max(row_ints) - min(row_ints)
        print(checksum)


if __name__ == "__main__":
    puzzle = ChecksumSolver()
    puzzle.main()
