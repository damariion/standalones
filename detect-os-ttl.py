from scapy.all import IP, ICMP, sr1
from sys import argv

class ICMP:

    @staticmethod
    def ttl(addr: str) -> int:
        
        # protocol procedure
        send = IP(dst = addr) / ICMP()
        recv = sr1(send, timeout = 1, verbose = 0)

        return recv[IP].ttl

class Program:

    map = \
    {
        64: "Unix",
        128: "Windows",
    }

    @classmethod
    def main(cls, addr):

        # response -> system
        system = cls.map[ICMP.ttl(addr)]
        print(f"{addr} is running {system}")

if __name__ == "__main__":
    
    # input handler
    if len(argv) == 2:
        Program.main(argv[1])