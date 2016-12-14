import re
import string
from operator import itemgetter


class RoomSecurity:

    def __init__(self):
        with open('input.txt', 'rt') as textfile:
            self.input = textfile.readlines()

    def get_verified_id(self, encrypted_name):
        room_name = re.search("^[A-Za-z\-]+", encrypted_name).group().replace('-', '')
        sector_id = re.search("-([0-9]+)\[", encrypted_name).group(1)
        checksum = re.search("\[([A-Za-z]+)\]", encrypted_name).group(1)

        letter_count = [[room_name.count(letter), letter] for letter in string.ascii_lowercase]
        top_letters = sorted(letter_count, reverse=True, key=itemgetter(0))[0:5]
        generated_checksum = ''.join(x[1] for x in top_letters)

        return int(sector_id) if generated_checksum == checksum else 0

    def main(self):
        id_sum = sum([self.get_verified_id(room_name) for room_name in self.input])
        print("Sum of IDs: %d" % id_sum)

if __name__ == "__main__":
    puzzle = RoomSecurity()
    puzzle.main()
