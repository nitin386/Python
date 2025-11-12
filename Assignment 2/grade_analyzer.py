# ============================================================
# Student Marks Analyzer
# Course: Foundations of Programming using Python (ETCCPP103)
# Project Title: Building a Student Marks Analyzer
# Name: Nitin
#Roll No: 2501720002
# ============================================================

import csv
from pathlib import Path

CSV_FILE = Path("grade.csv")
SUBJECTS = ["Subject-1", "Subject-2", "Subject-3", "Subject-4", "Subject-5"]


def ensure_csv_has_header() -> None:
    if not CSV_FILE.exists():
        with CSV_FILE.open("w", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(["Name", *SUBJECTS, "Total", "Average", "Grade", "Result"])


def grade_from_average(average: float) -> str:
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def result_from_average(average: float) -> str:
    return "Pass" if average >= 40 else "Fail"


def enter_marks_manually() -> None:
    ensure_csv_has_header()
    name = input("Enter the student name: ").strip()
    marks = []

    for subject in SUBJECTS:
        while True:
            try:
                score = float(input(f"Marks in {subject}: "))
                marks.append(score)
                break
            except ValueError:
                print("Please enter a valid number (e.g. 78.5).")

    total = sum(marks)
    average = total / len(marks)
    grade = grade_from_average(average)
    result = result_from_average(average)

    with CSV_FILE.open("a", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow([name, *marks, total, average, grade, result])

    print(f"Saved marks for {name} (Grade {grade}, {result}).\n")


def display_marks_from_csv() -> None:
    if not CSV_FILE.exists():
        print("No marks have been recorded yet.\n")
        return

    with CSV_FILE.open("r", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)

    if not rows:
        print("The marks file is empty.\n")
        return

    passed = failed = 0

    for row in rows:
        name = row["Name"]
        scores = [float(row[subject]) for subject in SUBJECTS]
        total = float(row.get("Total", sum(scores)))
        average = float(row.get("Average", total / len(scores)))
        grade = row.get("Grade", grade_from_average(average))
        result = row.get("Result") or result_from_average(average)

        if result == "Pass":
            passed += 1
        else:
            failed += 1

        print(f"\nName: {name}")
        for subject, score in zip(SUBJECTS, scores):
            print(f"  {subject}: {score}")
        print(f"  Total: {total}")
        print(f"  Average: {average:.2f}")
        print(f"  Grade: {grade}")
        print(f"  Result: {result}")

    print(f"\nTotal passed: {passed}")
    print(f"Total failed: {failed}\n")


def main() -> None:
    actions = {
        "1": enter_marks_manually,
        "2": display_marks_from_csv,
        "3": lambda: exit(0),
    }

    while True:
        print(
            "Menu:\n"
            "  1. Enter student marks manually\n"
            "  2. Read marks from the CSV file\n"
            "  3. Exit"
        )
        choice = input("Enter your choice: ").strip()
        action = actions.get(choice)

        if action:
            action()
        else:
            print("Invalid choice; please pick 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
