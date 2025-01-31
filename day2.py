import numpy as np
from utils.args import parse_args
from utils.extract import extract_ints


def is_safe(report):
    if report != sorted(report) and report != sorted(report, reverse=True):
        return False

    return all(1 <= diff <= 3 for diff in np.abs(np.diff(report)))


def damping(report):
    return any(is_safe(report[:i] + report[i + 1 :]) for i in range(len(report)))


def main(input):
    results = []
    damping_results = []
    with open(input, "r") as file:
        for line in file:
            report = extract_ints(line)
            results.append(is_safe(report))
            damping_results.append(damping(report))

    print(results.count(True))
    print(damping_results.count(True))


if __name__ == "__main__":
    args = parse_args(script="day2", description="Day 2 of Advent of Code 2024")
    if args.input:
        main(input=args.input)
    else:
        args.print_help()
