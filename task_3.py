# task_3 - logs generator

import argparse
import re

def parse_log_line(line: str) -> dict:
    # Розбиваємо лог-запис на компоненти
    parts = re.split(r'\s+', line, maxsplit=4)
    if len(parts) < 5:
        return {}
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[4]
    }

def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                log_dict = parse_log_line(line)
                if log_dict:
                    logs.append(log_dict)
    except FileNotFoundError:
        print(f"Помилка: файл '{file_path}' не існує.")
    except Exception as e:
        print(f"Виникла помилка: {e}")
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:    
    return [log for log in logs if log['level'] == level.upper()]

def count_logs_by_level(logs: list) -> dict:
    count = {}
    for log in logs:
        level = log['level']
        if level in count:
            count[level] += 1
        else:
            count[level] = 1
    return count

def display_log_counts(counts: dict):
    print(f"{'Рівень логування':<15} | {'Кількість'}")
    print("----------------------------")
    for level, count in counts.items():
    	print(f"{level:<16} | {count}")

def main():
    parser = argparse.ArgumentParser(description="Аналіз лог файлів та вивіод за рівнем логів")
    parser.add_argument("file_path", help="Шлях до файлу логів")
    parser.add_argument("level", nargs='?', help="Фільтер лог-файлів (наприклад, INFO, ERROR, DEBUG, WARNING).")
    args = parser.parse_args()

    logs = load_logs(args.file_path)
    if args.level:
    	print(f"Деталі логів для рівня {args.level.upper()}:")
    	logs = filter_logs_by_level(logs, args.level)
    	for log in logs:
    		print(f"{log['date']} {log['time']} {log['level']} {log['message']}")
    else:
        counts = count_logs_by_level(logs)
        display_log_counts(counts)

if __name__ == "__main__":
    main()