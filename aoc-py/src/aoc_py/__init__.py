import argparse
from pathlib import Path
from aoc_py import year2024
import glob

SOLUTIONS = {"year2024": {"day1": year2024.day1}}
HERE = Path(__file__).parent
DATAPATH = HERE / ".." / ".." / ".." / "data"


def main() -> None:
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
    files = [f for f in DATAPATH.resolve().glob("*") if f.is_file()]
    files = sorted(files)
    if args.test:
        func = module.test
        files = [file for file in files if "test" in str(file)]

    else:
        func = module.main
        files = [file for file in files if "task" in str(file)]
    # filepaths = [(DATAPATH / file).resolve() for file in files]
    func(*files)
