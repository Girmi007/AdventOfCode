import os
import csv

class PassphraseSolver:

    def __init__(self):
        input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
        with open(input_file_path, 'rt') as csvfile:
            reader = csv.reader(csvfile, skipinitialspace=True)
            self.instructions = list(reader)

    def main(self):
        unique_passphrases = [line[0] for line in self.instructions if len(line[0].split()) == len(set(line[0].split()))]
        print(len(unique_passphrases))


if __name__ == "__main__":
    puzzle = PassphraseSolver()
    puzzle.main()
