import os
import csv


class StackSolver:

    def __init__(self):
        input_file_path = os.path.join(os.path.dirname(__file__), 'input_test.txt')
        with open(input_file_path, 'rt') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t', skipinitialspace=True)
            self.instructions = list(reader)

        self.stack = [[]]

    def main(self):

        while self.instructions:
            for line in self.instructions:
                line_str = line[0]
                if not line_str.find(' -> ') == -1:
                    line_split = line_str.split(' -> ')
                    parent = line_split[0]
                    children = line_split[1].split()

                    level_max = len(self.stack)
                    for child in children:
                        for level_cnt in reversed(range(0, level_max)):
                            if child in self.stack[level_cnt]:
                                if level_cnt == level_max-1:
                                    self.stack.append([])

                                self.stack[level_cnt+1].append(parent)
                                self.instructions.remove(line_str)
                                break

                else:
                    self.stack[0].append(line_str)
                    self.instructions.remove(line)

                print(len(self.instructions))

        print(self.stack[-1][0])


if __name__ == "__main__":
    puzzle = StackSolver()
    puzzle.main()
