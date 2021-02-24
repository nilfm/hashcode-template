#!/usr/bin/env python3

import subprocess

def main():  
    args = "zip code.zip -r main.cc *.py optimizer cpp_utils".split()
    subprocess.run(args)

if __name__ == "__main__":
    main()