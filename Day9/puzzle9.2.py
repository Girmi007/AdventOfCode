import re


class Decompressor:

    def __init__(self):
        with open('input.txt', 'rt') as textfile:
            self.input = textfile.read().splitlines()[0]

    def decompressed_length(self, sequence):
        marker_match = re.search("\(([0-9]+)x([0-9]+)\)", sequence)

        if marker_match is None:
            length = len(sequence)
        else:
            index = marker_match.span()
            n_chars = int(marker_match.group(1))
            n_times = int(marker_match.group(2))
            nested_length = self.decompressed_length(sequence[index[1]:index[1] + n_chars])

            length = index[0] + nested_length * n_times + self.decompressed_length(sequence[index[1] + n_chars:])

        return length

    def main(self):
        total_length = self.decompressed_length(self.input)
        print("Output length: {}".format(total_length))

if __name__ == "__main__":
    puzzle = Decompressor()
    puzzle.main()
