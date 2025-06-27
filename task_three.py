import sys
from typing import List, Dict


def parse_log_line(line: str) -> Dict:
    """ Парсить один рядок логування так повертає словник з його компонентами. """

    try:
        parts = line.split(' ', 3)
        return {
            'date': parts[0],
            'time': parts[1],
            'level': parts[2],
            'message': parts[3].strip()
        }
    except IndexError:
        return None


def load_logs(file_path: str) -> List[Dict]:
    """ Завантажує та парсить лог-файл, повертаючи список словників. """

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            parsed_line = [parse_log_line(line) for line in file if line.strip()]
            return [log for log in parsed_line if log]
    except FileNotFoundError:
        print(f"Помилка: файл {file_path} не знайдено!")
        return []
    except Exception as e:
        print(f"Сталося помилка при читанні файлу: {e}")
        return []


def filter_logs_by_level(logs: List[Dict], level: str) -> List[Dict]:
    """ Фільтрує список логів за заданим рівнем. """

    return list(filter(lambda log: log['level'].lower() == level.lower(), logs))


def count_logs_by_level(logs: List[Dict]) -> Dict:
    """ Підраховує кількість записів для кожного рівня логування. """
    counts = {}

    for log in logs:
        level = log['level']
        counts[level] = counts.get(level, 0) + 1
    return counts


def display_log_counts(counts: Dict):
    """ Форматує та виводить статистику логів у вигляді таблиці. """
    print("Рівень лпгування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")


def main():
    """ Головна функція для обробки аргументів командного рядка та виклику інших функцій. """

    if len(sys.argv) < 2:
        print("Використання: Python task_three.py /шлях/до/sample.log [рівень_логування]")
        sys.exit(1)

    file_path = sys.argv[1]
    log_level_filter = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)

    if logs:
        counts = count_logs_by_level(logs)
        display_log_counts(counts)

        if log_level_filter:
            filtered_logs = filter_logs_by_level(logs, log_level_filter)
            print(f"\nДеталі логів для рівня {log_level_filter.upper()}:")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} {log['message']}")


if __name__ == "__main__":
    main()
