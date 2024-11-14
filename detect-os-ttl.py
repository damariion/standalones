from scapy.all import IP, ICMP, sr1
from sys import argv

class Core:

    map = \
    {
        64: "Unix",
        128: "Windows",
    }

    @staticmethod
    def icmp(addr: str) -> int:
        
        # protocol procedure
        send = IP(dst = addr) / ICMP()
        recv = sr1(send, timeout = 1, verbose = 0)

        return recv[IP].ttl

    @staticmethod
    def main(addr) -> None:

        # response -> system
        system = Core.map[Core.icmp(addr)]
        print(f"{addr} is running {system}")

if __name__ == "__main__":
    
    # basic-handler
    if len(argv) == 2:
        Core.main(argv[1])