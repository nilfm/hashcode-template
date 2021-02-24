#!/usr/bin/env python3

from optimizer.strategy import SimulatedAnnealingStrategy
from optimizer.utils import parse_arguments, parse_json, run_make, create_temp_file


def main():
    args = parse_arguments()
    run_make(args.executable)
    create_temp_file()
    params = parse_json(args.params)
    strategy = SimulatedAnnealingStrategy(params, args.steps, args.neighbours, args.lambda_exp, args.graph)
    strategy.execute(args.executable, args.data)


if __name__ == "__main__":
    main()
