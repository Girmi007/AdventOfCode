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
        while self.instructions:
            line = self.instructions[0]
            self.add_node_recursive(line)

        print(self.stack[-1][0])

    def add_node_recursive(self, line):
        line_split = line[0].split(' -> ')
        node_name = line_split[0]

        if len(line_split) == 1:
            current_level = 0

        else:
            children = line_split[1].split(', ')

            child_level = -2
            for instruc in self.instructions:
                if instruc[0].startswith(children[0]):
                    child_level = self.add_node_recursive(instruc)

            current_level = child_level+1

        if not len(self.stack) > current_level:
            for stack_level in range(len(self.stack), current_level+1):
                self.stack.append([])

        self.stack[current_level].append(node_name)
        self.instructions.remove(line)

        return current_level

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
