from scapy.all import IP, ICMP, sr1
from sys import argv

class Program:

    map = \
    {
        64: "Unix",
        128: "Windows",
    }

    def ttl(self, addr: str) -> int:
        
        # protocol procedure
        send = IP(dst = addr) / ICMP()
        recv = sr1(send, timeout = 1, verbose = 0)

        return recv[IP].ttl

    def main(self, addr):

        # response -> system
        system = self.map[self.ttl(addr)]
        print(f"{addr} is running {system}")

if __name__ == "__main__":
    
    # input handler
    if len(argv) == 2:
        (_ := Program()).main(argv[1])