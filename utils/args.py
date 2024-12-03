from argparse import ArgumentParser


def parse_args(script="day1", description="Day 1 of Advent of Code 2020"):
    parser = ArgumentParser(prog=script, description=description)
    parser.add_argument("input", help="Path to the input file")
    args = parser.parse_args()
    return args
