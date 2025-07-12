"""
import project class from project
import module datetime

constant filename = "projects.txt"

function main():
    print "welcome to pythonic project management"
    projects = load_projects(filename)
    print "loaded", length of projects, "projects from", filename

    menu = "- (l)oad projects\n- (s)ave projects\n- (d)isplay projects\n- (f)ilter projects by date\n- (a)dd new project\n- (u)pdate project\n- (q)uit"

    print menu
    choice = get user input and convert to lowercase

    while choice is not 'q':
        if choice is 'l':
            input filename from user
            projects = load_projects(filename)
        else if choice is 's':
            input filename from user
            save_projects(projects, filename)
        else if choice is 'd':
            display_projects(projects)
        else if choice is 'f':
            filter_projects_by_date(projects)
        else if choice is 'a':
            add_new_project(projects)
        else if choice is 'u':
            update_project(projects)
        else:
            print "invalid choice"
        print menu
        choice = get user input and convert to lowercase

    ask user if they want to save to default filename
    if yes:
        save_projects(projects, filename)
    else:
        print "no save performed"
    print "thank you for using custom-built project management software"

function load_projects(filename):
    open file for reading
    skip header line
    projects = []
    for each line in file:
        split line by tab
        if 5 parts exist:
            create project using parts
            add to projects list
    close file
    return projects

function save_projects(projects, filename):
    open file for writing
    write header line
    for each project in projects:
        write project.to_tab_delimited() to file
    close file

function display_projects(projects):
    incomplete = filter projects where not is_complete
    complete = filter projects where is_complete
    sort both lists by priority

    print "incomplete projects:"
    for each project in incomplete:
        print project

    print "completed projects:"
    for each project in complete:
        print project

function filter_projects_by_date(projects):
    input date string from user
    try:
        convert date string to date
        filtered = filter projects where start_date > filter_date
        sort filtered by start_date
        for each project in filtered:
            print project
    except:
        print "invalid date format"

function add_new_project(projects):
    print "let's add a new project"
    input name, date string, priority, cost, percent_complete
    convert date string to date
    create project using inputs
    append project to projects list

function update_project(projects):
    for index, project in projects:
        print index and project
    try:
        input index from user
        project = projects[index]
        print project
        input new percent_complete and priority (optional)
        if given, update project attributes
    except:
        print "invalid project choice"

if this is the main program:
    main()
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
