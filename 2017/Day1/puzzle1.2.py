import os
import csv


class CaptchSolver2:

    def __init__(self):

        input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
        with open(input_file_path, 'rt') as csvfile:
            reader = csv.reader(csvfile, skipinitialspace=True)
            self.instructions = list(reader)[0][0]
            self.look_ahead = len(self.instructions)//2

    def main(self):
        sum_nrs = 0
        for idx in range(0, self.look_ahead):
            current_nr = int(self.instructions[idx])
            match_nr = int(self.instructions[self.wrap_index(idx+self.look_ahead)])
            if current_nr == match_nr:
                sum_nrs += current_nr

        sum_nrs *= 2
        print(sum_nrs)

    def wrap_index(self, index):
        wrapped_index = index % (self.look_ahead*2)
        return wrapped_index


if __name__ == "__main__":
    puzzle = CaptchSolver2()
    puzzle.main()
