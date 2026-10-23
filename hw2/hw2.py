import csv


# Читаем файл
def read_file(file):
    with open(file, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f, delimiter=";")
        return list(reader)


# Отчет 1 (иерархия департаментов)
def report_1(employees):
    departments = {}

    for i in employees[1:]:
        department = i[1]
        team = i[2]

        if department not in departments:
            departments[department] = []

        if team not in departments[department]:
            departments[department].append(team)

    return departments


# Вывод отчета 1
def show_result_1(result):
    for department, teams in result.items():
        print("Департамент:", department)
        print("Отделы:")

        for team in teams:
            print(" -", team)

        print()


# Отчет 2 (сводка по департаментам)
def report_2(employees):
    departments = {}

    for i in employees[1:]:
        department = i[1]
        salary = int(i[5])

        if department not in departments:
            departments[department] = []

        departments[department].append(salary)

    result = {}

    for department, salaries in departments.items():
        count_emp = len(salaries)
        min_salary = min(salaries)
        max_salary = max(salaries)
        avg_salary = sum(salaries) / count_emp

        result[department] = [count_emp, min_salary, max_salary, avg_salary]

    return result


# Вывод отчета 2
def show_result_2(result):
    for department, stats in result.items():
        print("Департамент:", department)
        print("Количество сотрудников:", stats[0])
        print("Минимальный оклад:", stats[1])
        print("Максимальный оклад:", stats[2])
        print("Средний оклад:", round(stats[3], 2))
        print()


# Отчет 3 (сводка по департаментам в csv)
def report_3(employees, file="report_3.csv"):
    result = report_2(employees)

    with open(file, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f, delimiter=";")

        writer.writerow([
            "Департамент",
            "Количество сотрудников",
            "Минимальный оклад",
            "Максимальный оклад",
            "Средний оклад"
        ])

        for department, stats in result.items():
            writer.writerow([
                department,
                stats[0],
                stats[1],
                stats[2],
                round(stats[3], 2)
            ])
    print("Файл:", file)


# Основная функция
def main(variant: int):
    employees = read_file("Corp_Summary.csv")

    if variant == 1:
        result = report_1(employees)
        show_result_1(result)

    elif variant == 2:
        result = report_2(employees)
        show_result_2(result)

    elif variant == 3:
        report_3(employees)

    else:
        print("Неверный номер отчета, выберите 1, 2 или 3")


# Запускаем
if __name__ == '__main__':
    variant = int(input("Выберите номер отчета (1, 2 или 3): "))
    main(variant)