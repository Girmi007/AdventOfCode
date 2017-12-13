import os
import csv


class PassphraseSolver2:

    def __init__(self):
        input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
        with open(input_file_path, 'rt') as csvfile:
            reader = csv.reader(csvfile, skipinitialspace=True)
            self.instructions = [int(line[0]) for line in list(reader)]
            pass

    def main(self):
        instructions_length = len(self.instructions)

        loop_cnt = 0
        pointer = 0
        while pointer < instructions_length:
            memory_value = self.instructions[pointer]
            self.instructions[pointer] += 1
            pointer += memory_value
            loop_cnt += 1

        print(loop_cnt)


if __name__ == "__main__":
    puzzle = PassphraseSolver2()
    puzzle.main()
