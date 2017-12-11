import hashlib


class DoorIDPassword:

    def __init__(self):
        self.input = "uqwqemis"

    def main(self):
        password = ''
        i = 0

        while len(password) < 8:
            door_id = self.input + str(i)
            door_hash = hashlib.md5(door_id.encode('utf-8')).hexdigest()

            if door_hash[0:5] == "00000":
                password += door_hash[5]
                print(password)

            i += 1
        print("Password %s: " % password)


if __name__ == "__main__":
    puzzle = DoorIDPassword()
    puzzle.main()
