from common import common
import os
import sys
import pprint

def main():
    print("call main")
    common.comprehender("test").detect_language()

if __name__ == "__main__":
    main()