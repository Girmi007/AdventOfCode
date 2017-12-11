import re


class BathroomSecurity:

    def __init__(self):
        self.currentLocation = [0, 2]
        self.rowStart = {0: 1, 1: 2, 2: 5, 3: 10, 4: 13}

        with open('input.txt', 'rt') as textfile:
            self.input = textfile.read().splitlines()

    def select_next_key(self, instruction):
        absolute_direction = 0 if re.search(r'^[LR]$', instruction) else 1
        relative_direction = 1 if re.search(r'^[RD]$', instruction) else -1
        relative_direction_inv = 1 if re.search(r'^[LD]$', instruction) else -1

        summ = self.currentLocation[0] + self.currentLocation[1] + relative_direction
        diff = self.currentLocation[1] - self.currentLocation[0] + relative_direction_inv
        valid_move = 1 < summ < 7 and abs(diff) < 3

        self.currentLocation[absolute_direction] += relative_direction if valid_move else 0

    def get_current_key(self):
        a = self.rowStart[self.currentLocation[1]]
        b = self.currentLocation[0] - abs(self.currentLocation[1] - 2)

        key = a + b
        return key

    def main(self):
        code = ''
        for line in self.input:
            for instruction in line:
                self.select_next_key(instruction)

            code += str(self.get_current_key())
        print("Code: %s" % code)

if __name__ == "__main__":
    puzzle = BathroomSecurity()
    puzzle.main()
