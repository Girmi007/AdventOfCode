
class SpiralSolver2:

    def __init__(self):
        self.coord_list = [(0, 0, 1)]

    def main(self):
        stop_value = self.calculate_square_values(347991)
        print(stop_value)

    def calculate_square_values(self, limit):
        x_coord = 0
        y_coord = 0
        direction = 0  # 0 = right, 1 = up, 2 = left, 3 = down
        step_size = 1

        current_value = 0
        loop_cnt = 0
        step_cnt = 0
        while current_value < limit:
            x_coord, y_coord = self.calculate_relative_position(x_coord, y_coord, direction, 1)
            current_value = self.calculate_square_value(x_coord, y_coord)
            self.coord_list.append((x_coord, y_coord, current_value))

            loop_cnt += 1
            step_cnt += 1
            if step_cnt == step_size:
                direction = (direction + 1) % 4

            elif step_cnt == step_size*2:
                direction = (direction + 1) % 4
                step_size += 1
                step_cnt = 0

        return current_value

    @staticmethod
    def calculate_relative_position(x_coord, y_coord, direction, step_size):
        if direction % 2 == 0:
            x_coord += step_size if direction == 0 else -step_size
        else:
            y_coord += step_size if direction == 1 else -step_size

        return x_coord, y_coord

    def calculate_square_value(self, x_coord, y_coord):
        value = 0
        for x_offset in range(-1, 2):
            neighbor_x_coord = x_coord + x_offset
            for y_offset in range(-1, 2):
                if not (x_offset == 0 and y_offset == 0):
                    neighbor_y_coord = y_coord + y_offset
                    values = [coord[2] for coord in self.coord_list if
                              (coord[0] == neighbor_x_coord and coord[1] == neighbor_y_coord)]
                    value += values[0] if values else 0

        return value


if __name__ == "__main__":
    puzzle = SpiralSolver2()
    puzzle.main()
