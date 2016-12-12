import csv


class EasterBunnyHQBlocksTwo:

    def __init__(self):
        self.location = [0, 0]
        self.current_direction = 0
        self.visited_locations = set()

        with open('input.txt', 'rt') as csvfile:
            reader = csv.reader(csvfile, skipinitialspace=True)
            self.instructions = list(reader)[0]

    def turn(self, turn_direction):
        relative_turn = 1 if turn_direction == "R" else -1
        self.current_direction = (self.current_direction + relative_turn) % 4

    def step_and_check(self, step_size):
        for i in range(step_size):
            visited = self.step_single_and_check()
            if visited:
                return True
        return False

    def step_single_and_check(self):
        relative_step = 1 if self.current_direction % 3 else -1
        self.location[self.current_direction % 2] += relative_step

        if tuple(self.location) in self.visited_locations:
            return True
        else:
            self.visited_locations.add(tuple(self.location))
            return False

    def main(self):
        for instruction in self.instructions:
            self.turn(instruction[0])
            visited = self.step_and_check(int(instruction[1:]))
            if visited:
                break

        print("Distance: %d steps" % (abs(self.location[0]) + abs(self.location[1])))

if __name__ == "__main__":
    puzzle = EasterBunnyHQBlocksTwo()
    puzzle.main()
