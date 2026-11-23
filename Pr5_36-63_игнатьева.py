import json
import os

input_file = 'students.json'
output_file = 'report.json'

report_data = {
    "students": [],
    "total_average": 0
}

total_sum = 0
total_count = 0

if not os.path.exists(input_file):
    print(f"Ошибка: Файл {input_file} не найден.")
else:
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            students = json.load(f)

        if not isinstance(students, list):
            raise ValueError("Данные в файле не являются списком.")

        for student in students:
            if not isinstance(student, dict):
                print("Предупреждение: Пропущен элемент, который не является словарем.")
                continue

            if 'name' not in student or 'grades' not in student:
                print(f"Предупреждение: У студента отсутствует имя или оценки: {student}")
                continue

            name = student['name']
            grades = student['grades']

            if not isinstance(name, str) or not isinstance(grades, list):
                print(f"Предупреждение: Неверный тип данных у студента {name}.")
                continue

            if len(grades) > 0 and not all(isinstance(g, (int, float)) for g in grades):
                print(f"Предупреждение: Оценки студента {name} содержат не числа.")
                continue

            if len(grades) > 0:
                student_avg = sum(grades) / len(grades)
            else:
                student_avg = 0

            report_data["students"].append({
                "name": name,
                "average": round(student_avg, 2)
            })

            total_sum += sum(grades)
            total_count += len(grades)

        if total_count > 0:
            report_data["total_average"] = round(total_sum / total_count, 2)
        else:
            report_data["total_average"] = 0

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, ensure_ascii=False, indent=4)

        print(f"Отчет успешно сохранен в {output_file}")

    except FileNotFoundError:
        print("ошибка: файл students.json не найден.")
    except json.JSONDecodeError:
        print("ошибка: students.json содержит некорректный JSON.")
    except (KeyError, TypeError, ValueError) as error:
        print(f"ошибка в данных: {error}")
    except OSError as error:
        print(f"ошибка при работе с файлом: {error}")