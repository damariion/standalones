from hashlib import md5
from sys import argv

class Hash:

    def __init__(self, target):
        self.target = target

    def compare(self, attempt: str) -> bool:
        
        # transform
        attempt = attempt.encode()
        attempt = md5(attempt).hexdigest()

        # compare
        return attempt == self.target

class Program:

    def main(target, words):
        
        # set target hash
        thash = Hash(target)

        # bruteforce
        with open(words, 'r') as file:
            
            for word in file.readlines():
                
                if not thash.compare(word):
                    continue

                # cracked
                print(f'"{target}" is "{word}"')
                break

if __name__ == "__main__":

    # input handler
    if len(argv) == 3:
        Program.main(argv[1], argv[2])