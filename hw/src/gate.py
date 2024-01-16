import argparse
from data import DATA

def main():
    parser = argparse.ArgumentParser(description="Process data and compute statistics.")
    parser.add_argument("-f", "--file", type=str, help="Path to the input CSV file.")
    parser.add_argument("-t", "--type", type=str, help="Type of statistics to compute.")

    args = parser.parse_args()

    if args.file is None or args.type is None:
        print("Please provide both file path and type of statistics.")
        return

    data = DATA(args.file)

    if args.type == "stats":
        compute_statistics(data)
    else:
        print(f"Invalid statistics type: {args.type}")

def compute_statistics(data):
    result = {}

    for col in data.cols.all:
        col_type = 'y' if hasattr(col, 'y') else 'x'
        result[col.at] = {
            "mean": col_type == 'y' and col.mid() or None,
            "mode": col_type == 'y' and col.mode() or None
        }

    print("Mean and Mode for each column:")
    print(result)

if __name__ == "__main__":
    main()
