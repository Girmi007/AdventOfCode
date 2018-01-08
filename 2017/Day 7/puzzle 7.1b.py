import os
import csv


class StackSolver:

    def __init__(self):
        input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
        with open(input_file_path, 'rt') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t', skipinitialspace=True)
            self.instructions = list(reader)

        self.stack = [[]]

    def main(self):
        for line in self.instructions:
            node_name, node_level = self.determine_level(line)

            if not len(self.stack) > node_level:
                for stack_level in range(len(self.stack), node_level+1):
                    self.stack.append([])

            self.stack[node_level].append(node_name)

        print(self.stack[-1][0])

    def determine_level(self, line):
        line_split = line[0].split(' -> ')
        if len(line_split) == 1:
            current_level = 0

        else:
            children = line_split[1].split(', ')

            child_line = ''
            for instr in self.instructions:
                if instr[0].startswith(children[0]):
                    child_line = instr
                    break
            child_name, child_level = self.determine_level(child_line)

            current_level = child_level+1

        return line_split[0], current_level


if __name__ == "__main__":
    puzzle = StackSolver()
    puzzle.main()
