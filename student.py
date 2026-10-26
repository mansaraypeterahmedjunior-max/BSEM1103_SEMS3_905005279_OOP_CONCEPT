"""
Student-Registration-System
student.py

Contains the Student class. A Student object stores student information
and behaves like a registered student (it can log in and register for
modules).
"""


class Student:
    """Represents a university student."""

    # Smallest and largest accepted age for a university student.
    MIN_AGE = 15
    MAX_AGE = 100

    def __init__(self, student_id, name, age, username, password):
        """Constructor: create the attributes of a new Student object."""
        self.student_id = student_id      # String, e.g. "ST001"
        self.name = name                  # String, e.g. "Mohamed"
        self.age = age                    # Integer, e.g. 20
        self.username = username          # String, e.g. "mohamed01"
        self.password = password          # String (prototype only)
        self.registered_modules = []      # List that will hold Module objects

    # ---------------------------------------------------------- INSTANCE METHODS

    def display_info(self):
        """Instance method: print the information of this student."""
        print("=" * 40)
        print("STUDENT INFORMATION")
        print("-" * 40)
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Username:", self.username)
        print("Modules registered:", len(self.registered_modules))
        print("=" * 40)

    def login(self, username, password):
        """
        Instance method: check login details.
        Returns True if the details match this student, otherwise False.
        """
        return username == self.username and password == self.password

    def register_module(self, module):
        """
        Instance method: add a Module object to this student's list.
        Returns True if the module was added, False if it was already there.
        """
        for registered in self.registered_modules:
            if registered.module_code == module.module_code:
                return False  # Do not register the same module twice
        self.registered_modules.append(module)
        return True

    # ------------------------------------------------------------- CLASS METHOD

    @classmethod
    def create_student(cls, student_id, name, age, username, password):
        """
        Class method: create and return a Student object.
        Example: student1 = Student.create_student("ST001", "Mohamed", 20, "mohamed01", "python123")
        """
        student = cls(student_id, name, age, username, password)
        return student

    # ------------------------------------------------------------ STATIC METHOD

    @staticmethod
    def validate_age(age):
        """
        Static method: check that the age is an integer between
        MIN_AGE (15) and MAX_AGE (100). Returns True or False.
        """
        return Student.MIN_AGE <= age <= Student.MAX_AGE
