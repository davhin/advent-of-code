from collections import defaultdict


def main(f) -> None:
    print(f"The solution is {solve1(f)}")
    print(f"The solution is {solve2(f)}")


def test(f) -> None:
    assert solve1(f) == 11
    assert solve2(f) == 31


def load_columns(f):
    lines = f.read_text().splitlines()
    pairs = [tuple(map(int, line.split())) for line in lines]
    left = sorted([pair[0] for pair in pairs])
    right = sorted([pair[1] for pair in pairs])
    return left, right


def min_zip_iter(a, b):
    a_iter = iter(sorted(a))
    b_iter = iter(sorted(b))
    try:
        a_val = next(a_iter)
        b_val = next(b_iter)
        while True:
            yield a_val, b_val
            a_val = next(a_iter)
            b_val = next(b_iter)
    except StopIteration:
        return


def solve1(f):
    left, right = load_columns(f)
    return sum([abs(x - y) for x, y in zip(left, right)])


def solve2(f):
    left, right = load_columns(f)
    right_counts = defaultdict(lambda: 0)
    for n in right:
        right_counts[n] += 1
    return sum([n * right_counts[n] for n in left])
