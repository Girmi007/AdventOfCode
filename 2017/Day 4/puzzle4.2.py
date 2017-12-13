import os
import csv

class PassphraseSolver2:

    def __init__(self):
        input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
        with open(input_file_path, 'rt') as csvfile:
            reader = csv.reader(csvfile, skipinitialspace=True)
            self.instructions = list(reader)

    def main(self):
        passphrase_count = 0
        for line in self.instructions:
            word_sets = [frozenset(word) for word in line[0].split()]
            line_set = set(word_sets)
            if len(word_sets) == len(line_set):
                passphrase_count += 1

        print(passphrase_count)


if __name__ == "__main__":
    puzzle = PassphraseSolver2()
    puzzle.main()
