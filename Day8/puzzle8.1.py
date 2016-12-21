import numpy as np
import re


class LittleScreen:

    def __init__(self):
        self.screen = np.zeros([6, 50])

        with open('input.txt', 'rt') as textfile:
            self.input = textfile.read().splitlines()

    def parse_input(self, input_line):
        split_line = input_line.split()

        if split_line[0] == "rect":
            size = re.search("(\d+)x(\d+)", split_line[1])
            self.draw_rectangle(int(size.group(1)), int(size.group(2)))
        elif split_line[0] == "rotate":
            line = re.search("[xy]=(\d+)", split_line[2]).group(1)
            self.rotate_line(split_line[1], int(line), int(split_line[4]))

    def draw_rectangle(self, width, height):
        self.screen[0:height, 0:width] = 1

    def rotate_line(self, row_column, line, amount):
        if row_column == "row":
            self.screen[line, :] = np.roll(self.screen[line, :], amount)
        elif row_column == "column":
            self.screen[:, line] = np.roll(self.screen[:, line], amount)

    def print_screen(self):
        [print(''.join(["[%s]" % ('#' if column else ' ') for column in row])) for row in self.screen]

    def main(self):
        [self.parse_input(line) for line in self.input]
        self.print_screen()
        lit_pixels = sum([1 if column else 0 for row in self.screen for column in row])
        print("Lit pixels: %d" % lit_pixels)

if __name__ == "__main__":
    puzzle = LittleScreen()
    puzzle.main()
