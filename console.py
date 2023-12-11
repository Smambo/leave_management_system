#!/usr/bin/python3
#Import modules for classes
import sys
import datetime


class LeaveManagementSystem():
    """created LMS class"""

    
    def __init__(self):
        """initialises class"""
        self.users = []
        self.employees = []
        self.admins = []

    def run(self):
        """checks if LMS is running"""
        while (True):
            input_str = input("LMS> ")
            if (input_str.startswith("login")):
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                self.login(username, password)
            elif (input_str.startswith("request leave")):
                start = input("Enter leave start date (YYYY-MM-DD): ")
                end = input("Enter leave end date (YYYY-MM-DD): ")
                reason = input("Enter reason for leave: ")
                self.request_leave(start, end, reason)
            elif (input_str.startswith("help")):
                self.print_help()
            elif (input_str.startswith("exit")):
                print("Goodbye!\n")
                break

    def login(self, username, password):
        print("{} logged in!".format(username))

    def print_help(self):
        print("""
              Leave Management System - Help

              Available commands:
              login - Log in with your username and password
              request leave - Request a leave by providing start date, end date and reason 
              help - Print this help message
              exit - Exit the leave management system

              After login, employees can also:
              request leave - Request a new leave
              check status - Check status of previously requested leaves

              After login, administrators can also: 
              approve leave <request_id> - Approve a leave request 
              reject leave <request_id> - Reject a leave request
              view requests - View all pending requests""")

    def get_current_employee(self):
        """checks if current user is an employee"""
        

    def request_leave(self, start, end, reason):
        employee = self.get_current_employee()
        leave_request = employee.request_leave(start, end, reason)
        print("Leave request created!")

class User:
    """Created User class."""
    def __init__(self, username, password):
        """Initialises class."""
        self.username = username
        self.password = password

    def login(self, username, password):
        """verifies login credentials"""
        if (self.username == username and self.password == password):
            print("{} successfully logged in!\n".format(username))
            return (True)
        else:
            print("Login credentials invalid!\n")
            return (False)

class Employee(User):
    """
    Created Employee class.
    Inherits from User class.
    """
    def __init__(self, name, email, role, username, password):
        """Initialises employee class."""
        self.name = name
        self.email = email
        self.role = role
        super().__init__(username, password)

    def request_leave(self, start, end, reason):
        """Need to validate requested leave dates"""
        leave_request = RequestedLeave(self, start, end, reason)
        return (leave_request)


class RequestedLeave:
    """Creates class"""
    def __init__(self, employee, start, end, reason):
        """initialises requestedleave class."""
        self.employee = employee
        self.start = start
        self.end = end
        self.reason = reason
        self.status = "Pending"

    def approved(self):
        """approves leave"""
        self.status = "Approved!\n"

    def rejected(self):
        """rejects leave"""
        self.status = "Rejected!\n"


class Admin(User):
    """
    Creates Admin class.
    Inherits from User class.
    """
    def __init__(self, name, email, username, password):
        """initialises admin class"""
        self.name = name
        self.email = email
        super().__init__(username, password)

    def review_request(self, leave_request):
        """Review employee leave request"""
        print("Reviewing leave request for {} from {} to {}. Reason for leave: {}".format(leave_request.employee.name, leave_request.start, leave_request.end, leave_request.reason))

    def approve_request(self, leave_request):
        """Approve employee leave request"""
        leave_request.approved()
        print("Approved leave request for {}".format(leave_request.employee.name))

    def reject_request(self, leave_request):
        """Reject employee leave request"""
        leave_request.rejected()
        print("Rejected leave request for {}".format(leave_request.employee.name))

"""
employee1 = Employee("Nikola Tesla", "nikola@tesla.com", "Software Engineer", "nikola", "Hello123")
admin1 = Admin("Elon Musk", "elon@tesla.com", "elon", "Mars101")
employee1.login("nikola", "Hello123")
admin1.login("elon", "Mars101")

employee2 = Employee("Dev Ops", "dev@tesla.com", "System Administrator", "dev", "CiCd")
admin2 = Admin("Mae Musk", "mae@tesla.com", "mae", "admin2")
employee2.login("dev", "CiCd")
admin2.login("mae", "admin2")

leave_request1 = employee1.request_leave(datetime.date(2023, 6, 1), datetime.date(2023, 6, 15), "Annual Leave")
leave_request2 = employee2.request_leave(datetime.date(2021, 6, 2), datetime.date(2023, 6, 15), "Indefinite Hiatus")

admin1.review_request(leave_request1)
admin1.approve_request(leave_request1)
print(leave_request1.status)

admin2.review_request(leave_request2)
admin2.reject_request(leave_request2)
print(leave_request2.status)
"""


lms = LeaveManagementSystem()
lms.run()
