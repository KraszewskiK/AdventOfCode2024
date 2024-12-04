def solve_part1(input_data: str) -> int:
    reports = input_data.split("\n")
    reports = [[int(x) for x in report.split() if x.strip()] for report in reports]
    safe_reports = [report for report in reports if is_report_safe(report)]
    return len(safe_reports)


def solve_part2(input_data: str) -> int:
    reports = input_data.split("\n")
    reports = [[int(x) for x in report.split() if x.strip()] for report in reports]
    safe_reports = []
    for report in reports:
        if is_report_safe(report):
            safe_reports.append(report)
        else:
            for i in range(len(report)):
                if is_report_safe(report[:i] + report[i + 1:]):
                    safe_reports.append(report)
                    break
    return len(safe_reports)


def is_report_safe(report: list[int]) -> bool:
    if len(report) < 2:
        return True

    incr = 1 if report[0] < report[1] else -1

    for i in range(1, len(report)):
        if not 1 <= (report[i] - report[i - 1]) * incr <= 3:
            return False

    return True
