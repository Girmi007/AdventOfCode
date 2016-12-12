import csv
import re


class BathroomSecurity:

    def __init__(self):
        self.currentLocation = [1, 1]

        with open('input.txt', 'rt') as csvfile:
            reader = csv.reader(csvfile, skipinitialspace=True)
            self.input = list(reader)

    def select_next_key(self, instruction):
        absolute_direction = 0 if re.search(r'^[LR]$', instruction) else 1
        relative_direction = 1 if re.search(r'^[RD]$', instruction) else -1
        valid_move = (self.currentLocation[absolute_direction] + relative_direction) % 4 < 3

        self.currentLocation[absolute_direction] += relative_direction if valid_move else 0

    def get_current_key(self):
        key = self.currentLocation[1] * 3 + self.currentLocation[0] + 1
        return key

    def main(self):
        code = []
        for line in self.input:
            for instruction in line[0]:
                self.select_next_key(instruction)

            code.append(self.get_current_key())
        print(''.join(str(x) for x in code))

if __name__ == "__main__":
    puzzle = BathroomSecurity()
    puzzle.main()
