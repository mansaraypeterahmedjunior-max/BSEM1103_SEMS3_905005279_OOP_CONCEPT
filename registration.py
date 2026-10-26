"""
Student-Registration-System
registration.py

Contains the Registration class. A Registration object is the link between
a Student object and a Module object. This is the demonstration of object
interaction in this project: Registration receives a Student object and a
Module object and works with both of them.
"""


class Registration:
    """Represents the relationship between one Student and one Module."""

    def __init__(self, student, module):
        """Constructor: store the Student object and the Module object."""
        self.student = student  # A Student object
        self.module = module    # A Module object

    def display_registration(self):
        """Instance method: print who registered for which module."""
        print("=" * 40)
        print("MODULE REGISTRATION")
        print("-" * 40)
        print("Student:", self.student.name, "(", self.student.student_id, ")")
        # Ask the Module object to display itself -> objects work together.
        self.module.display_module()
        print("=" * 40)
