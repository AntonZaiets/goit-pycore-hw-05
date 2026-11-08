import sys
from collections import defaultdict


# parse log line
def parse_log_line(line: str) -> dict:
    line_split = line.strip().split(" ", 3)
    return {
        "date": line_split[0],
        "time": line_split[1],
        "level": line_split[2],
        "message": line_split[3]
    }


# load logs from file
def load_logs(file_path: str) -> list:
    with open(file_path, "r", encoding="utf-8") as file:
        return [parse_log_line(line) for line in file if line.strip()]


# filter logs by level
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log["level"] == level.upper()]


# count logs by level
def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)
    for log in logs:
        counts[log["level"]] += 1
    return counts


# display log counts
def display_log_counts(counts: dict):
    print(f"{'Рівень логування':<17}| Кількість")
    print(f"{'-' * 17}|{'-' * 10}")
    for level, count in counts.items():
        print(f"{level:<17}| {count}")


# main function
def main():
    if len(sys.argv) < 2:
        print("Usage: python task_3.py <log_file> [level]")
        sys.exit(1)

    file_path = sys.argv[1]
    level = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        logs = load_logs(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)
    except IndexError:
        print("Invalid log file format.")
        sys.exit(1)
    except (OSError, UnicodeDecodeError) as error:
        print(f"Error reading file: {error}")
        sys.exit(1)

    display_log_counts(count_logs_by_level(logs))

    if level:
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        for log in filter_logs_by_level(logs, level):
            print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()
