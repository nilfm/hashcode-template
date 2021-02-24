import argparse
import json
import subprocess

from optimizer.parameter import IntParameter, FloatParameter
from optimizer.get_score import compute_score


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--params",
        help="Path to JSON file with the names and bounds of the parameters",
        type=str,
        required=True,
    )
    parser.add_argument(
        "-d",
        "--data",
        help="Path to the file with the input data",
        type=str,
        required=True,
    )
    parser.add_argument(
        "-s",
        "--steps",
        help="Number of iterations of the method (default: 1000)",
        type=int,
        default=1000,
    )
    parser.add_argument(
        "-x",
        "--executable",
        help="Path to the executable file (from C++)",
        type=str,
        default="main",
    )
    parser.add_argument(
        "-n",
        "--neighbours",
        help="Number of neighbours that will be attempted unsuccessfully in SA before ending the execution",
        type=int,
        default=25,
    )
    parser.add_argument(
        "-l",
        "--lambda_exp",
        help="Multiplies the exponent in SA. Bigger lambdas imply less volatility. Must be positive. Default: 10",
        type=float,
        default=10,
    )
    parser.add_argument(
        "-g",
        "--graph",
        help="Show a plot with the evolution of the score at the end. Boolean.",
        action="store_true",
    )
    return parser.parse_args()


def parse_json(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)

    params = []
    for item in data["floats"]:
        params.append(
            FloatParameter(
                item["name"], item["lower"], item["upper"]
            )
        )
    for item in data["ints"]:
        params.append(
            IntParameter(
                item["name"], item["lower"], item["upper"]
            )
        )
    return params


def run_cpp(params, executable, data_path):
    args = [f"./{executable}", f"inputs/{data_path}"] + params
    subprocess.run(args)


def run_make(executable):
    subprocess.run(["make", executable])


def create_temp_file():
    subprocess.run(["touch", "out_temp.txt"])