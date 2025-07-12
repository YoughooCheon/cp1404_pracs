"""
import module datetime

function create_project(name, start_date, priority, cost_estimate, percent_complete):
    if start_date is string:
        start_date = parse start_date using format "dd/mm/yyyy"
    project = {
        "name": name,
        "start_date": start_date,
        "priority": to_integer(priority),
        "cost_estimate": to_float(cost_estimate),
        "percent_complete": to_integer(percent_complete)
    }
    return project

function is_complete(project):
    return project["percent_complete"] == 100

function project_less_than(project1, project2):
    return project1["priority"] < project2["priority"]

function project_to_string(project):
    return project["name"] + ", start: " + format_date(project["start_date"], "dd/mm/yyyy") + ", priority " + str(project["priority"]) + ", estimate: $" + format_number(project["cost_estimate"], 2) + ", completion: " + str(project["percent_complete"]) + "%"

function project_to_tab_delimited(project):
    return project["name"] + "\t" + format_date(project["start_date"], "dd/mm/yyyy") + "\t" + str(project["priority"]) + "\t" + str(project["cost_estimate"]) + "\t" + str(project["percent_complete"])
"""

import datetime

class Project:
    """Class to represent a project with start date, priority, cost and completion."""

    def __init__(self, name, start_date, priority, cost_estimate, percent_complete):
        """Initialise a Project instance."""
        self.name = name
        if isinstance(start_date, str):
            self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        else:
            self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.percent_complete = int(percent_complete)

    def is_complete(self):
        """Return True if the project is 100% complete."""
        return self.percent_complete == 100

    def __lt__(self, other):
        """Compare projects based on priority (lower is higher priority)."""
        return self.priority < other.priority

    def __str__(self):
        """Return string representation for display."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.percent_complete}%")

    def to_tab_delimited(self):
        """Return a tab-delimited string suitable for saving to file."""
        return f"{self.name}\t{self.start_date.strftime('%d/%m/%Y')}\t{self.priority}\t{self.cost_estimate}\t{self.percent_complete}"
