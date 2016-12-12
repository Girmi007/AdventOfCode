import csv


class EasterBunnyHQ:

    def __init__(self):
        self.x = 0
        self.y = 0
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
        if self.current_direction % 2:
            self.x += relative_step
        else:
            self.y += relative_step

        if (self.x, self.y) in self.visited_locations:
            return True
        else:
            self.visited_locations.add((self.x, self.y))
            return False

    def main(self):
        for instruction in self.instructions:
            self.turn(instruction[0])
            visited = self.step_and_check(int(instruction[1:]))
            if visited:
                break

        print("Distance: %d steps" % (abs(self.x) + abs(self.y)))

if __name__ == "__main__":
    puzzle = EasterBunnyHQ()
    puzzle.main()
