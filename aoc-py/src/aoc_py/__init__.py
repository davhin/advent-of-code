import argparse
from pathlib import Path
from aoc_py import year2024

SOLUTIONS = {"year2024": {"day1": year2024.day1}}
HERE = Path(__file__).parent
DATAPATH = HERE / ".." / ".." / ".." / "data"


def main() -> None:
    import sys

    print("Arguments received:", sys.argv)
    global DATAPATH
    parser = argparse.ArgumentParser(description="My CLI")
    parser.add_argument("year", help="AoC year")
    parser.add_argument("day", help="AoC day")
    parser.add_argument(
        "--test", action="store_true", help="whether to execute only test"
    )
    args = parser.parse_args()
    module = SOLUTIONS[args.year][args.day]
    DATAPATH = DATAPATH / args.year / args.day
    if args.test:
        func = module.test
        filepath = (DATAPATH / "test.txt").resolve()
    else:
        func = module.main
        filepath = (DATAPATH / "main.txt").resolve()
    func(filepath)
