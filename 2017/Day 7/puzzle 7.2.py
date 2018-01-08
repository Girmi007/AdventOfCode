import os
import csv


class StackSolver2:

    def __init__(self):
        input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
        with open(input_file_path, 'rt') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t', skipinitialspace=True)
            self.instructions = list(reader)

        self.stack = [[]]

    def main(self):
        root_node = self.find_root()
        self.add_nodes_recursive(root_node)
        print(self.stack[-1][0])

    def add_nodes_recursive(self, line):
        line_split = line[0].split(' -> ')
        node_name = line_split[0]

        if len(line_split) == 1:
            current_level = 0

        else:
            children = line_split[1].split(', ')

            child_level = -2
            for instruc in self.instructions:
                if instruc[0].startswith(children[0]):
                    child_level = self.add_nodes_recursive(instruc)

            current_level = child_level+1

        if not len(self.stack) > current_level:
            for stack_level in range(len(self.stack), current_level+1):
                self.stack.append([])

        self.stack[current_level].append(node_name)
        self.instructions.remove(line)

        return current_level

    def find_root(self):
        all_nodes = []
        for line in self.instructions:
            line_split = line[0].split(' -> ')
            node = line_split[0].split()[0]
            all_nodes.append(node)

            if len(line_split) > 1:
                child_nodes = line_split[1].split(', ')
                for child in child_nodes:
                    all_nodes.append(child)

        for line in self.instructions:
            line_split = line[0].split(' -> ')
            node = line_split[0].split()[0]
            if all_nodes.count(node) == 1:
                return line


if __name__ == "__main__":
    puzzle = StackSolver2()
    puzzle.main()
