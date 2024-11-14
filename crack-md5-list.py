from hashlib import md5
from sys import argv

class this:

    @staticmethod
    def compare(attempt: str, target: str) -> bool:
        
        # transform
        attempt = attempt.encode()
        attempt = md5(attempt).hexdigest()

        # compare
        return attempt == target

    @staticmethod
    def main(target, words) -> None:
        
        with open(words, 'r') as file:
            
            for word in file.readlines():
                
                if not this.compare(word, target):
                    continue

                # cracked
                print(f'"{target}" is "{word}"')
                break

if __name__ == "__main__":

    # input handler
    if len(argv) == 3:
        this.main(argv[1], argv[2])