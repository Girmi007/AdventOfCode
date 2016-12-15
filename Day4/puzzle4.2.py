import re
import string
from operator import itemgetter


class RoomSecurity:

    def __init__(self):
        with open('input.txt', 'rt') as textfile:
            self.input = textfile.read().splitlines()

    def decrypt_room_name(self, encrypted_name):
        sector_id = int(re.search("-([0-9]+)\[", encrypted_name).group(1))
        checksum = re.search("\[([A-Za-z]+)\]", encrypted_name).group(1)
        room_name = re.search("^[A-Za-z\-]+", encrypted_name).group().replace('-', ' ')

        letter_count = [[room_name.count(letter), letter] for letter in string.ascii_lowercase]
        top_letters = sorted(letter_count, reverse=True, key=itemgetter(0))[0:5]
        generated_checksum = ''.join(x[1] for x in top_letters)

        shifted_room_name = ''.join([self.shift_letter(letter, sector_id) for letter in room_name])
        return (shifted_room_name, sector_id) if generated_checksum == checksum else None

    def shift_letter(self, letter, shift):
        shifted = chr(((ord(letter) - 97 + shift) % 26) + 97)
        return shifted if letter in string.ascii_lowercase else letter

    def main(self):
        decrypted_names = [self.decrypt_room_name(room_name) for room_name in self.input]
        decrypted_names = [name for name in decrypted_names if name is not None]
        north_pole_room = [room_name for room_name in decrypted_names if re.match("north|pole", room_name[0])]
        print("North pole room: %s, id: %d" % north_pole_room[0])

if __name__ == "__main__":
    puzzle = RoomSecurity()
    puzzle.main()
