#!/usr/bin/pythom3
import sys
if __name__ == "__main__":
     main()

def main():
    count = len(sys.argv) - 1
    argv = sys.argv[1:]
    print("Number of argument{}: {}".format('' if count == 1 else 's', count), end='')
    if count == 0:
        print('.', end='\n\n')
    else:
        print(':')
        for i, arg in enumerate(argv, 1):
            print("{}: {}".format(i, arg))
