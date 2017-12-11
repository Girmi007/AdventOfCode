import hashlib


class DoorIDPassword:

    def __init__(self):
        self.input = "uqwqemis"

    def main(self):
        password = ['']*8
        i = 0

        while len(''.join(password)) < 8:
            door_id = self.input + str(i)
            door_hash = hashlib.md5(door_id.encode('utf-8')).hexdigest()

            position = int(door_hash[5], 16)
            if door_hash[0:5] == "00000" and position < 8 and not password[position]:
                password[position] = door_hash[6]

            i += 1
        print("Password %s: " % ''.join(password))


if __name__ == "__main__":
    puzzle = DoorIDPassword()
    puzzle.main()
