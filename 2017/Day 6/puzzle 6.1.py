import os
import csv
import numpy as np


class MemoryReallocator:

    def __init__(self):
        input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
        with open(input_file_path, 'rt') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t', skipinitialspace=True)
            self.current_memory_layout = [int(mem) for mem in list(reader)[0]]
            self.memory_size = len(self.current_memory_layout)

        self.observed_layouts = []

    def main(self):

        cylce_cnt = 0
        while self.current_memory_layout not in self.observed_layouts:
            self.observed_layouts.append(list(self.current_memory_layout))

            max_idx = np.asscalar(np.argmax(self.current_memory_layout))
            max_val = self.current_memory_layout[max_idx]

            self.current_memory_layout[max_idx] = 0
            for cnt in range(1, max_val+1):
                idx = (max_idx+cnt) % self.memory_size
                self.current_memory_layout[idx] += 1

            cylce_cnt += 1

        print(cylce_cnt)


if __name__ == "__main__":
    puzzle = MemoryReallocator()
    puzzle.main()
