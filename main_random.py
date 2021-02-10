#!/usr/bin/env python3

from optimizer.strategy import RandomStrategy
from optimizer.utils import parse_arguments, parse_json, run_make


def main():
    args = parse_arguments()
    run_make(args.executable)
    params = parse_json(args.params)
    strategy = RandomStrategy(params, args.steps, args.graph)
    strategy.execute(args.executable, args.data)


if __name__ == "__main__":
    main()
