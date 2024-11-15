from hashlib import md5
from sys import argv

class Program:

    def compare(self, attempt: str, target: str) -> bool:
        
        # transform
        attempt = attempt.encode()
        attempt = md5(attempt).hexdigest()

        # compare
        return attempt == target

    def main(self, target, words):
        
        with open(words, 'r') as file:
            
            for word in file.readlines():
                
                if not self.compare(word, target):
                    continue

                # cracked
                print(f'"{target}" is "{word}"')
                break

if __name__ == "__main__":

    # input handler
    if len(argv) == 3:
        (_ := Program()).main(argv[1], argv[2])