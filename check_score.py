#!/usr/bin/env python3

import sys
from optimizer.get_score import compute_score

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 check_score.py <output file name>")
        return
    
    score = compute_score(sys.argv[1])
    print(f"Score for {sys.argv[1]}: {score}")

if __name__ == "__main__":
    main()