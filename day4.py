from utils.args import parse_args

WORDS = ["XMAS", "SMAX"]


def get_grid_point(matriz, x, y):
    if x < 0 or y < 0:
        return "."
    try:
        return matriz[y][x]
    except IndexError:
        return "."


def find_horizontal(matriz, x, y):
    find = "".join([get_grid_point(matriz, x + i, y) for i in range(4)])
    return find in WORDS


def find_vertical(matriz, x, y):
    find = "".join([get_grid_point(matriz, x, y + i) for i in range(4)])
    return find in WORDS


def find_backwards_horizontal(matriz, x, y):
    find = "".join([get_grid_point(matriz, x - i, y) for i in range(4)])
    return find in WORDS


def find_backwards_vertical(matriz, x, y):
    find = "".join([get_grid_point(matriz, x, y - i) for i in range(4)])
    return find in WORDS


def find_left_diagonal(matriz, x, y):
    find = "".join([get_grid_point(matriz, x - i, y + i) for i in range(4)])
    return find in WORDS


def find_right_diagonal(matriz, x, y):
    find = "".join([get_grid_point(matriz, x + i, y + i) for i in range(4)])
    return find in WORDS


def find_left_backwards_diagonal(matriz, x, y):
    if x - 4 < 0 or y - 4 < 0:
        return False  # Out of bounds
    find = "".join([get_grid_point(matriz, x - i, y - i) for i in range(4)])
    return find in WORDS


def find_right_backwards_diagonal(matriz, x, y):
    find = "".join([get_grid_point(matriz, x + i, y - i) for i in range(4)])
    return find in WORDS


def main(input):
    with open(input) as f:
        matriz = [list(line.rstrip()) for line in f.readlines()]

    finds = 0
    for y in range(len(matriz)):
        for x in range(len(matriz[y])):
            if find_horizontal(matriz, x, y):
                finds += 1
            if find_vertical(matriz, x, y):
                finds += 1

            if find_backwards_horizontal(matriz, x, y):
                finds += 1
            if find_backwards_vertical(matriz, x, y):
                finds += 1

            if find_left_diagonal(matriz, x, y):
                finds += 1
            if find_right_diagonal(matriz, x, y):
                finds += 1

            if find_left_backwards_diagonal(matriz, x, y):
                finds += 1
            if find_right_backwards_diagonal(matriz, x, y):
                finds += 1

    print(finds)


if __name__ == "__main__":
    args = parse_args()
    if args.input:
        main(args.input)
    else:
        args.print_help()
