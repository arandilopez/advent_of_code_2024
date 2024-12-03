import pandas as pd
import numpy as np
from .utils.args import parse_args


def main(input):
    data = pd.read_csv(input, names=["first", "second"], sep=r"\s+", engine="python")
    for col in data:
        data[col] = data[col].sort_values(ignore_index=True)

    diff = np.sum(np.abs(data["first"] - data["second"]))
    print(diff)

    second_list_counts = data["second"].value_counts()
    similarity_score = np.sum(
        [i * (second_list_counts.get(i) or 0) for i in data["first"]]
    )
    print(similarity_score)


if __name__ == "__main__":
    args = parse_args(script="day1", description="Day 1 of Advent of Code 2024")
    if args.input:
        main(input=args.input)
    else:
        args.print_help()
