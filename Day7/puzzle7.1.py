import re


class IPv7:

    def __init__(self):
        with open('input.txt', 'rt') as textfile:
            self.input = textfile.read().splitlines()

    def supports_tls(self, ip):
        supernets = [result[1] for result in re.findall("(^|\])([A-Za-z]+?)(\[|$)", ip)]
        hypernets = re.findall("\[([A-Za-z]+?)\]", ip)

        supernetss_abba = [part for part in supernets if self.contains_abba(part)]
        hypernets_abba = [part for part in hypernets if self.contains_abba(part)]

        return len(supernetss_abba) > 0 and len(hypernets_abba) == 0

    def contains_abba(self, ip_part):
        abbas = [ip_part[i:i+4] for i in range(0, len(ip_part)-4) if ip_part[i:i+2] == ip_part[i+2:i+4][::-1]]
        return len(abbas) > 0

    def main(self):
        tls_count = sum([1 for ip in self.input if self.supports_tls(ip)])
        print("IPs supporting TLS: %d" % tls_count)

if __name__ == "__main__":
    puzzle = IPv7()
    puzzle.main()
