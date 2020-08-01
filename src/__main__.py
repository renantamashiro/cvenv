import sys

import cvenv


def main():
    args = sys.argv
    getattr(cvenv, args[1])(args[2])

if __name__ == '__main__':
    main()
