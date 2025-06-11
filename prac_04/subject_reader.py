FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_details(data)


def load_data():
    """Read data from file formatted like: subject, lecturer, number of students."""
    data_list = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()  # Remove the newline character
            parts = line.split(',')  # Split data into a list
            parts[2] = int(parts[2])  # Convert student number to an integer
            data_list.append(parts)  # Append the processed list to the main list
    return data_list


def display_subject_details(data):
    """Display subject details in the required format."""
    for subject, lecturer, student_count in data:
        print(f"{subject} is taught by {lecturer} and has {student_count} students")


main()
