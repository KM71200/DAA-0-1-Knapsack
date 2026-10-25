import re
import sys
import time
import os
from pathlib import Path


def parse_tests(text):
    sections = re.split(r"(?m)^\s*#Test\b[^\n]*$", text)
    tests = []

    for section in sections:
        rows = []

        for line in section.splitlines():
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            try:
                values = [int(part) for part in line.split()]
            except ValueError:
                raise ValueError(f"Invalid input line: {line}")

            rows.append(values)

        if not rows:
            continue

        if len(rows[0]) != 2:
            raise ValueError("The first data line must contain n and W.")

        n, capacity = rows[0]

        if n < 0 or capacity < 0:
            raise ValueError("n and W must be non-negative.")

        item_rows = rows[1:]

        if len(item_rows) != n:
            raise ValueError(f"Expected {n} items, but found {len(item_rows)}.")

        items = []

        for row in item_rows:
            if len(row) != 2:
                raise ValueError("Each item must contain exactly two integers: weight value.")

            weight, value = row

            if weight < 0:
                raise ValueError("Item weights cannot be negative.")

            items.append((weight, value))

        tests.append((n, capacity, items))

    if not tests:
        raise ValueError("No valid test cases found.")

    return tests


def render_table(dp, items, capacity, current_i, current_w):
    

    headers = ["Item / Capacity"] + [
        str(w) for w in range(capacity + 1)
    ]

    table = [headers]

    for i in range(len(items) + 1):

        if i == 0:
            label = "No items"
        else:
            weight, value = items[i - 1]
            label = f"Item {i} (w={weight}, v={value})"

        row = [label]

        for w in range(capacity + 1):

            
            if i == 0:
                row.append(str(dp[i][w]))

            
            elif i < current_i or (i == current_i and w < current_w):
                row.append(str(dp[i][w]))

       
            elif i == current_i and w == current_w:
                row.append(f"[{dp[i][w]}]")

           
            else:
                row.append(".")

        table.append(row)


    widths = [
        max(len(row[col]) for row in table)
        for col in range(len(headers))
    ]

    border = "+" + "+".join("-" * (width + 2) for width in widths) + "+"

    output = [border]

    for row in table:
        output.append("| "+ " | ".join(
                row[col].center(widths[col])
                for col in range(len(row))
            ) + " |"
        )

        output.append(border)

    return "\n".join(output)


def knapsack(capacity, items, visualize=True, delay=0.01):
    n = len(items)


    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    if visualize:
        print("\nInitial DP table:")

        print(
            render_table(
                dp, items, capacity, 0, -1
            )
        )

        print("\n. = Not calculated yet")
        print("[x] = Current cell being calculated")

        time.sleep(delay)

   
    for i in range(1, n + 1):

        weight, value = items[i - 1]

       
        for w in range(capacity + 1):

            dp[i][w] = dp[i - 1][w]

            if weight <= w:

                dp[i][w] = max(
                    dp[i][w],
                    value + dp[i - 1][w - weight]
                )

            if visualize:
                os.system("cls" if os.name == "nt" else "clear")

                print(
                    f"0/1 KNAPSACK - Item {i}/{n}\n"
                    f"Current item: weight={weight}, value={value}\n"
                    f"Calculating dp[{i}][{w}]\n"
                )

                print(render_table(dp, items, capacity, i, w))

                print(
                    "\nNumbers = Calculated cells"
                    " | [x] = Current cell"
                    " | . = Not calculated"
                )

                sys.stdout.flush()
                time.sleep(delay)

    if visualize:

        os.system("cls" if os.name == "nt" else "clear")

        print("FINAL DP TABLE\n")

        print(render_table(dp, items, capacity, n, capacity))

        print(
            f"\nMaximum value = dp[{n}][{capacity}]"
            f" = {dp[n][capacity]}"
        )

    return dp[n][capacity]


def main():

    if len(sys.argv) > 1:

        input_path = Path(sys.argv[1])

        try:
            input_text = input_path.read_text(encoding="utf-8")

        except OSError as error:
            print(f"Could not read input file: {error}")
            raise SystemExit(1)

    else:
        input_text = sys.stdin.read()

    if not input_text.strip():

        print(
            "No input provided.\n"
            'Run: python knapsack_visualizer_live.py '
            '"Knapsack data (2).txt"'
        )

        raise SystemExit(1)

    try:

        tests = parse_tests(input_text)

        result_lines = []

        for test_number, (n, capacity, items) in enumerate(
            tests, start=1
        ):

            print(
                f"\n{'=' * 12} TEST CASE "
                f"{test_number} {'=' * 12}"
            )

            print(f"Number of items: {n}")
            print(f"Knapsack capacity: {capacity}")

            answer = knapsack(
                capacity,
                items,
                visualize=True,
                delay=0.05
            )

            print(
                f"\nTest case {test_number} result: {answer}"
            )

            result_lines.append(
                f"#Test case {test_number} input "
                f"({n} {capacity}) test result {answer}"
            )

        Path("result.txt").write_text("\n".join(result_lines) + "\n",encoding="utf-8")

        print("\nAll results saved successfully to result.txt")

    except (ValueError, OSError) as error:

        print(f"Error: {error}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()