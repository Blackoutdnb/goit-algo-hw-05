from typing import List, Dict
import sys


# Parse a single log line into components
def parse_log_line(line: str) -> Dict[str, str]:
    parts = line.strip().split(maxsplit=3)
    if len(parts) < 4:
        return {}

    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3],
    }


# Load logs from file into a list of dictionaries
def load_logs(file_path: str) -> List[Dict[str, str]]:
    logs = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            record = parse_log_line(line)
            if record:
                logs.append(record)
    return logs


# Filter logs by logging level
def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    return [log for log in logs if log["level"] == level]


# Count number of logs per level
def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1
    return counts


# Display formatted table with log counts
def display_log_counts(counts: Dict[str, int]) -> None:
    print("Рівень логування | Кількість")
    print("-----------------|----------")

    ordered_levels = ["INFO", "DEBUG", "ERROR", "WARNING"]
    for level in ordered_levels:
        print(f"{level:<16} | {counts.get(level, 0)}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python main.py /path/to/logfile.log [ERROR|INFO|WARNING|DEBUG]")
        return

    file_path = sys.argv[1]
    level = sys.argv[2].upper() if len(sys.argv) >= 3 else None

    # Validate log level if provided
    valid_levels = {"INFO", "DEBUG", "ERROR", "WARNING"}
    if level and level not in valid_levels:
        print("Unknown log level. Use: INFO, DEBUG, ERROR, WARNING")
        return

    # Load logs with error handling
    try:
        logs = load_logs(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return
    except OSError as e:
        print(f"Error reading file: {e}")
        return

    # Count and display statistics
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    # If level specified → show detailed logs
    if level:
        filtered = filter_logs_by_level(logs, level)

        print(f"\nДеталі логів для рівня '{level}':")

        if not filtered:
            print("0 записів знайдено")
            return

        for log in filtered:
            print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()
