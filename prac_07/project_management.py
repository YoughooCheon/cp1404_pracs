"""

"""
from project import Project
import datetime

FILENAME = "projects.txt"

def main():
    """Main function to run the project management menu interface."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""

    print(MENU)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'l':
            filename = input("Enter filename to load from: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter filename to save to: ")
            save_projects(projects, filename)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input(">>> ").lower()

    save_choice = input(f"Would you like to save to {FILENAME}? ").lower()
    if save_choice in ['yes', 'y']:
        save_projects(projects, FILENAME)
    else:
        print("No save performed.")
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from a tab-delimited file and return a list of Project objects."""
    projects = []
    with open(filename, 'r') as file:
        next(file)
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) == 5:
                project = Project(*parts)
                projects.append(project)
    return projects

def save_projects(projects, filename):
    """Save the current list of projects to a tab-delimited file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(project.to_tab_delimited() + "\n")

def display_projects(projects):
    """Display incomplete and completed projects, sorted by priority."""
    incomplete = sorted([p for p in projects if not p.is_complete()])
    complete = sorted([p for p in projects if p.is_complete()])

    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")

    print("Completed projects:")
    for project in complete:
        print(f"  {project}")

def filter_projects_by_date(projects):
    """Filter and display projects that start after a given date."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    try:
        filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        filtered = sorted(
            [p for p in projects if p.start_date > filter_date],
            key=lambda p: p.start_date
        )
        for project in filtered:
            print(project)
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")

def add_new_project(projects):
    """Prompt user for project details and add a new project to the list."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date_str = input("Start date (dd/mm/yy): ")
    start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    percent_complete = int(input("Percent complete: "))
    project = Project(name, start_date, priority, cost_estimate, percent_complete)
    projects.append(project)


def update_project(projects):
    """Prompt user to choose a project and update its completion or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        index = int(input("Project choice: "))
        project = projects[index]
        print(project)
        percent_input = input("New Percentage: ")
        if percent_input:
            project.percent_complete = int(percent_input)
        priority_input = input("New Priority: ")
        if priority_input:
            project.priority = int(priority_input)
    except (ValueError, IndexError):
        print("Invalid project choice.")

if __name__ == '__main__':
    main()
