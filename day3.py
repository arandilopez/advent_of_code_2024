import re
from utils.args import parse_args


def parse_instructions(text):
    return re.findall(r"mul\(\d+,\d+\)", text)


def sum_instructions(instructions):
    return sum([a * b for a, b in map(extract_ints, instructions)])


def extract_ints(match):
    return list(map(int, re.findall(r"-?\d+", match)))


def part1(text):
    instructions = parse_instructions(text)
    return sum_instructions(instructions)


def part2(text):
    re_enable_pattern = r"(don't\(\).*?do\(\)|don't\(\).*)"

    enabled = re.sub(re_enable_pattern, "", text)

    instructions = parse_instructions(enabled)
    return sum_instructions(instructions)


def main(input):
    with open(input, "r") as file:
        text = file.read().strip().replace("\n", "")
        print(part1(text))
        print(part2(text))


if __name__ == "__main__":
    args = parse_args(script="day3", description="Day 3 of Advent of Code 2024")
    if args.input:
        main(input=args.input)
    else:
        args.print_help()
