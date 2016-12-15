import re
import itertools

class IPv7:

    def __init__(self):
        with open('input.txt', 'rt') as textfile:
            self.input = textfile.read().splitlines()

    def supports_ssl(self, ip):
        supernets = [result[1] for result in re.findall("(^|\])([A-Za-z]+?)(\[|$)", ip)]
        hypernets = re.findall("\[([A-Za-z]+?)\]", ip)

        supernets_abas = [self.get_abas(part) for part in supernets]
        supernets_abas = list(itertools.chain.from_iterable(supernets_abas))  # flatten list

        supernets_babs = [self.aba_to_bab(aba) for aba in supernets_abas]
        hypernets_maching_babs = [bab for bab in supernets_babs for hypernet in hypernets if bab in hypernet]
        return len(hypernets_maching_babs) > 0

    def get_abas(self, ip_part):
        abas = [ip_part[i:i+3] for i in range(len(ip_part)-2) if self.is_aba(ip_part[i:i+3])]
        return abas

    def is_aba(self, ip_part):
        return ip_part[0] == ip_part[2] and ip_part[0] != ip_part[1]

    def aba_to_bab(self, aba):
        return aba[1] + aba[0] + aba[1]

    def main(self):
        tls_count = sum([1 for ip in self.input if self.supports_ssl(ip)])
        print("IPs supporting TLS: %d" % tls_count)

if __name__ == "__main__":
    puzzle = IPv7()
    puzzle.main()
