import csv


class EasterBunnyHQBlocks:

    def __init__(self):
        self.location = [0, 0]
        self.current_direction = 0

        with open('input.txt', 'rt') as csvfile:
            reader = csv.reader(csvfile, skipinitialspace=True)
            self.instructions = list(reader)[0]

    def turn(self, turn_direction):
        relative_turn = 1 if turn_direction == "R" else -1
        self.current_direction = (self.current_direction + relative_turn) % 4

    def step(self, step_size):
        relative_step = step_size if self.current_direction % 3 else -step_size
        self.location[self.current_direction % 2] += relative_step

    def main(self):
        for instruction in self.instructions:
            self.turn(instruction[0])
            self.step(int(instruction[1:]))

        print("Distance: %d steps" % (abs(self.location[0]) + abs(self.location[1])))

if __name__ == "__main__":
    puzzle = EasterBunnyHQBlocks()
    puzzle.main()
