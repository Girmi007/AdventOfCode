
class SpiralSolver:

    def __init__(self):
        pass

    def main(self):
        x_coord, y_coord = self.calculate_square_location(347991)
        steps = self.manhattan_distance(x_coord, y_coord)
        print(steps)

    def calculate_square_location(self, square_value):
        x_coord = 0
        y_coord = 0
        direction = 0  # 0 = right, 1 = up, 2 = left, 3 = down
        step_size = 1

        distance_remaining = square_value-1
        loop_cnt = 0
        while distance_remaining >= step_size:
            x_coord, y_coord = self.calculate_relative_position(x_coord, y_coord, direction, step_size)
            distance_remaining -= step_size

            loop_cnt += 1
            direction = (direction + 1) % 4
            if loop_cnt % 2 == 0:
                step_size += 1

        x_coord, y_coord = self.calculate_relative_position(x_coord, y_coord, direction, distance_remaining)

        return x_coord, y_coord

    @staticmethod
    def calculate_relative_position(x_coord, y_coord, direction, step_size):
        if direction % 2 == 0:
            x_coord += step_size if direction == 0 else -step_size
        else:
            y_coord += step_size if direction == 1 else -step_size

        return x_coord, y_coord

    @staticmethod
    def manhattan_distance(x_coord, y_coord):
        return abs(x_coord) + abs(y_coord)



if __name__ == "__main__":
    puzzle = SpiralSolver()
    puzzle.main()
