
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


def get_valid_marks():
    while True:
        try:
            marks = float(input("Enter marks out of 100: "))

            if 0 <= marks <= 100:
                return marks

            print("Error: Marks must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    print("\n===== STUDENT GRADE CALCULATOR =====")

    name = input("Enter student name: ").strip()

    while not name:
        print("Name cannot be empty.")
        name = input("Enter student name: ").strip()

    marks = get_valid_marks()
    grade = calculate_grade(marks)

    status = "Pass" if grade != "F" else "Needs Improvement"

    print("\n===== STUDENT RESULT =====")
    print(f"Student Name : {name}")
    print(f"Marks        : {marks:g}/100")
    print(f"Grade        : {grade}")
    print(f"Status       : {status}")
    print("===========================")


if __name__ == "__main__":
    main()
