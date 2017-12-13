import os
import csv


class ChecksumSolver2:

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
            for nr_idx in range(0, len(row_ints)):
                for remaining_nr in row_ints[nr_idx+1:]:
                    if row_ints[nr_idx] % remaining_nr == 0:
                        checksum += row_ints[nr_idx] // remaining_nr
                        break
                    elif remaining_nr % row_ints[nr_idx] == 0:
                        checksum += remaining_nr // row_ints[nr_idx]
                        break
        print(checksum)


if __name__ == "__main__":
    puzzle = ChecksumSolver2()
    puzzle.main()
