import os
import csv
import re


class CaptchSolver:

    def __init__(self):

        input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
        with open(input_file_path, 'rt') as csvfile:
            reader = csv.reader(csvfile, skipinitialspace=True)
            self.instructions = list(reader)[0][0]

    def main(self):
        regex = re.compile(r'(\d)\1+')
        number_groups = regex.finditer(self.instructions)
        group_values = [(len(group.group(0))-1) * int(group.group(0)[0]) for group in number_groups if len(group.group(0)) > 1]
        sum_sizes = sum(group_values)

        if self.instructions[0] == self.instructions[-1]:
            sum_sizes += int(self.instructions[0])

        print(sum_sizes)


if __name__ == "__main__":
    puzzle = CaptchSolver()
    puzzle.main()
