"""
Student-Registration-System
module.py

Contains the Module class. A Module object represents an academic module
offered by the university. All module information below is fictional and
is used only for demonstration.
"""


class Module:
    """Represents an academic module offered by the university."""

    def __init__(self, module_code, module_name, credit_units):
        """Constructor: create the attributes of a new Module object."""
        self.module_code = module_code      # String, e.g. "CS101"
        self.module_name = module_name      # String, e.g. "Introduction to Programming"
        self.credit_units = credit_units    # Integer, e.g. 3

    def display_module(self):
        """Instance method: print this module in a readable single line."""
        print(f"{self.module_code} | {self.module_name} | {self.credit_units} Credits")
