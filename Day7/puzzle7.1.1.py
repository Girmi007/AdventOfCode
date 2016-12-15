import re
import math


class IPv7:

    def __init__(self):
        with open('input.txt', 'rt') as textfile:
            self.input = textfile.read().splitlines()

    def supports_tls(self, ip):
        supernets = [result[1] for result in re.findall("(^|\])([A-Za-z]+?)(\[|$)", ip)]
        hypernets = re.findall("\[([A-Za-z]+?)\]", ip)

        supernets_abba = [part for part in supernets if self.contains_abba(part)]
        hypernets_abba = [part for part in hypernets if self.contains_abba(part)]

        return len(supernets_abba) > 0 and len(hypernets_abba) == 0

    def contains_abba(self, ip_part):
        abbas = [ip_part[i:i+4] for i in range(0, len(ip_part)-4) if self.is_abba(ip_part[i:i+4])]
        return len(abbas) > 0

    def is_abba(self, ip_part):
        l = len(ip_part)
        if l % 2 == 0:
            return ip_part[0:int(l/2)] == ip_part[-int(l/2):][::-1]
        else:
            return ip_part[0:math.floor(l/2)] == ip_part[-math.ceil(l/2):][::-1]

    def main(self):
        tls_count = sum([1 for ip in self.input if self.supports_tls(ip)])
        print("IPs supporting TLS: %d" % tls_count)

if __name__ == "__main__":
    puzzle = IPv7()
    puzzle.main()
