import hashlib


class DoorIDPassword:

    def __init__(self):
        self.input = "abc"
        self.password_list = []

    def door_hash_generator(self):
        i = 0
        while len(self.password_list) < 8:
            door_id = self.input + str(i)
            door_hash = hashlib.md5(door_id.encode('utf-8')).hexdigest()
            yield door_hash
            i += 1

    def main(self):
        door_hasher = self.door_hash_generator()
        # Does not work, list won't be filled gradually, so generator can't check and will loop forever
        password_list = [door_hash[5] for door_hash in door_hasher if door_hash[0:5] == "00000"]

        print("Password %s: " % ''.join(password_list))


if __name__ == "__main__":
    puzzle = DoorIDPassword()
    puzzle.main()
