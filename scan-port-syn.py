from sys import argv
from threading import Thread
from scapy.all import IP, TCP, sr1
from socket import gethostname, gethostbyname

class Scanner:

    local = gethostbyname(gethostname())
    popen = 0

    def __init__(self, addr):
        self.remote = addr

    def syn(self, rport, lport=65533) -> object | None:

        ip = IP(
            src=self.local, 
            dst=self.remote
            )
        
        tcp = TCP(
            sport=lport, 
            dport=rport, 
            flags="S"
            )
        
        # receive response
        if (response := sr1(ip / tcp, timeout=1, verbose=0)):
            
            # complete variables
            text = f"port {rport} is open\n"
            self.popen += 1

            # display
            print(text if response.ack else "", end='')


class Program:

    @staticmethod
    def main(addr):

        scanner = Scanner(addr)
        threads = [
            Thread(target=scanner.syn, args=(i,)) 
            for i in range(1, 1023)
            ]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        print(f"\nscan complete ({scanner.popen} ports are open)")

if __name__ == "__main__":

    if len(argv) == 2:
        Program.main(argv[1])