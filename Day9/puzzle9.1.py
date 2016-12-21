import numpy as np
import re


class Decompressor:

    def __init__(self):
        self.pointer = 0
        self.output = ''
        with open('input.txt', 'rt') as textfile:
            self.input = textfile.read().splitlines()[0]

    def decompress(self):
        while self.pointer < len(self.input):
            if self.input[self.pointer] == '(':
                marker = ' '
                while self.input[self.pointer] != ')':
                    marker += self.input[self.pointer]
                    self.pointer += 1
                self.pointer += 1

                marker_match = re.search("([0-9]+)x([0-9]+)", marker)
                n_chars = int(marker_match.group(1))
                n_times = int(marker_match.group(2))

                self.output += self.expand(n_chars, n_times)
                self.pointer += n_chars
            else:
                self.output += self.input[self.pointer]
                self.pointer += 1

    def expand(self, n_chars, n_times):
        substr = self.input[self.pointer:self.pointer + n_chars]
        return substr * n_times

    def main(self):
        self.decompress()
        print("Output length: %d" % len(self.output))

if __name__ == "__main__":
    puzzle = Decompressor()
    puzzle.main()
