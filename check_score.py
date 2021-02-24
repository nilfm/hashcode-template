#!/usr/bin/env python3

import sys
from optimizer.get_score import compute_score

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 check_score.py <output file name>")
        return
    
    name = sys.argv[1]
    input_path = f"inputs/{name}"
    output_path = f"outputs/{name}_output.txt"
    score = compute_score(input_path, output_path)
    print(f"Score for {name}: {score}")

if __name__ == "__main__":
    main()