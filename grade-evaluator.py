import csv
import sys
import os


def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists,
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")

    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

    assignments = []

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })

        if not assignments:
            print("Error: CSV file is empty.")
            sys.exit(1)

        return assignments

    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)


def evaluate_grades(data):
    """
    Calculates final grade, GPA, pass/fail status,
    and resubmission eligibility.
    """

    print("\n--- Processing Grades ---")

    # Validate scores
    for assignment in data:
        if assignment['score'] < 0 or assignment['score'] > 100:
            print(
                f"Error: Invalid score {assignment['score']} "
                f"for {assignment['assignment']}."
            )
            return

    # Validate weights
    total_weight = 0
    formative_weight = 0
    summative_weight = 0

    for assignment in data:
        total_weight += assignment['weight']

        if assignment['group'] == "Formative":
            formative_weight += assignment['weight']

        elif assignment['group'] == "Summative":
            summative_weight += assignment['weight']

    if abs(total_weight - 100) > 0.01:
        print(f"Error: Total weight is {total_weight}, expected 100.")
        return

    if abs(formative_weight - 60) > 0.01:
        print(
            f"Error: Formative weight is {formative_weight}, expected 60."
        )
        return

    if abs(summative_weight - 40) > 0.01:
        print(
            f"Error: Summative weight is {summative_weight}, expected 40."
        )
        return

    # Calculate final grade
    total_grade = 0

    for assignment in data:
        total_grade += (
            assignment['score'] * assignment['weight']
        ) / 100

    print(f"Final Grade: {total_grade:.2f}%")

    # Calculate GPA
    gpa = (total_grade / 100) * 5.0

    print(f"GPA: {gpa:.2f}")

    # Calculate category scores
    formative_score = 0
    summative_score = 0

    for assignment in data:
        weighted_score = (
            assignment['score'] * assignment['weight']
        ) / 100

        if assignment['group'] == "Formative":
            formative_score += weighted_score

        elif assignment['group'] == "Summative":
            summative_score += weighted_score

    formative_average = (formative_score / formative_weight) * 100
    summative_average = (summative_score / summative_weight) * 100

    print(f"Formative Score: {formative_average:.2f}%")
    print(f"Summative Score: {summative_average:.2f}%")

    # Determine pass/fail
    if formative_average >= 50 and summative_average >= 50:
        print("Status: PASSED")
    else:
        print("Status: FAILED")

    # Find failed formative assignments for resubmission
    failed_formative = []

    for assignment in data:
        if (
            assignment['group'] == "Formative"
            and assignment['score'] < 50
        ):
            failed_formative.append(assignment)

    if failed_formative:
        highest_weight = failed_formative[0]['weight']

        for assignment in failed_formative:
            if assignment['weight'] > highest_weight:
                highest_weight = assignment['weight']

        print("\nEligible assignment(s) for resubmission:")

        for assignment in failed_formative:
            if assignment['weight'] == highest_weight:
                print(
                    f"- {assignment['assignment']} "
                    f"(Weight: {assignment['weight']}%)"
                )

    else:
        print("\nNo formative resubmission required.")


if __name__ == "__main__":

    # Load the data
    course_data = load_csv_data()

    # Process the grades
    evaluate_grades(course_data)
