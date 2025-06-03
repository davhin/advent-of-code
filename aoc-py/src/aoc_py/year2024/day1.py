def main(f) -> None:
    print(f"The solution is {solve(f)}")


def test(f) -> None:
    assert solve(f) == 11


def solve(f):
    lines = f.read_text().splitlines()
    pairs = [tuple(map(int, line.split())) for line in lines]
    left = sorted([pair[0] for pair in pairs])
    right = sorted([pair[1] for pair in pairs])
    return sum([abs(x - y) for x, y in zip(left, right)])
