"""
Student-Registration-System
main.py

Program entry point. Run the program with:

    python main.py

The program is a simple console application that lets a student:
1. Register as a new student.
2. Log in with a username and password.
3. View the modules offered by the university.
4. Register for modules.
5. View the modules they have registered for.
6. Log out and exit.

Only Python standard functionality is used. There is no database, no GUI
and no external package. All data is kept in plain lists and disappears
when the program is closed.
"""

from student import Student
from module import Module
from registration import Registration


# ----------------------------------------------------------- INPUT FUNCTIONS
# Small functions that use input() and validate what the user types.

def read_text(prompt):
    """Read a piece of text that must not be empty."""
    while True:
        value = input(prompt).strip()
        if value == "":
            print("Input cannot be empty. Please try again.")
        else:
            return value


def read_name(prompt):
    """Read a student name. The name must contain letters, not only numbers."""
    while True:
        name = input(prompt).strip()
        if name == "":
            print("Name cannot be empty. Please try again.")
        elif not name.replace(" ", "").isalpha():
            print("Name must contain letters, not numbers only.")
        else:
            return name


def read_age(prompt):
    """Read a whole number age between 15 and 100."""
    while True:
        age_text = input(prompt).strip()
        try:
            age = int(age_text)      # Letters or decimals cause a ValueError
        except ValueError:
            print("Age must be a whole number. Please try again.")
            continue
        if Student.validate_age(age):  # static method of the Student class
            return age
        print("Age must be between 15 and 100. Please try again.")


def read_choice(prompt, valid_choices):
    """Read a menu choice and only accept one of the valid choices."""
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print("Please enter a valid option.")


def read_unique_username(students):
    """Read a username that is not already used by another student."""
    while True:
        username = read_text("Username: ")
        for student in students:
            if student.username == username:
                print("That username is already taken. Please choose another.")
                break
        else:
            # The loop finished without a break, so the username is free.
            return username


def read_unique_student_id(students):
    """Read a student ID that is not already used by another student."""
    while True:
        student_id = read_text("Student ID: ")
        for student in students:
            if student.student_id == student_id:
                print("That student ID is already registered. Please use another.")
                break
        else:
            return student_id


# ------------------------------------------------------------ HELP FUNCTIONS

def username_exists(students, username):
    """Search the students list for a username."""
    for student in students:
        if student.username == username:
            return True
    return False


def find_student(students, username):
    """Search the students list and return the matching Student object."""
    for student in students:
        if student.username == username:
            return student
    return None


def find_module(modules, module_code):
    """Search the modules list and return the matching Module object."""
    for module in modules:
        if module.module_code == module_code.upper():
            return module
    return None


def create_available_modules():
    """Create the Module objects offered by the university (fictional data)."""
    modules = []
    modules.append(Module("CS101", "Introduction to Programming", 3))
    modules.append(Module("CS102", "Database Systems", 3))
    modules.append(Module("SE201", "Object-Oriented Programming", 3))
    modules.append(Module("SE202", "Web Development", 3))
    modules.append(Module("SE203", "Computer Networks", 3))
    return modules


def display_available_modules(modules):
    """Print every Module object in the modules list."""
    print("\n" + "=" * 40)
    print("AVAILABLE MODULES")
    print("-" * 40)
    number = 1
    for module in modules:
        print(f"{number}. ", end="")
        module.display_module()      # ask the Module object to display itself
        number += 1
    print("=" * 40)


def display_registered_modules(student):
    """Print the Module objects stored in the student's registered_modules list."""
    print("\n" + "=" * 40)
    print("MY REGISTERED MODULES")
    print("-" * 40)
    if len(student.registered_modules) == 0:
        print("You have not registered for any module yet.")
    else:
        number = 1
        for module in student.registered_modules:
            print(f"{number}. ", end="")
            module.display_module()
            number += 1
        total_credits = 0
        for module in student.registered_modules:
            total_credits += module.credit_units
        print("-" * 40)
        print("Total modules:", len(student.registered_modules))
        print("Total credit units:", total_credits)
    print("=" * 40)


# ------------------------------------------------------------ SYSTEM ACTIONS

def register_student(students):
    """Ask for student information with input() and create a Student object."""
    print("\n" + "=" * 40)
    print("STUDENT REGISTRATION")
    print("-" * 40)

    student_id = read_unique_student_id(students)     # kept as text, e.g. ST001
    name = read_name("Name: ")
    age = read_age("Age: ")
    username = read_unique_username(students)
    password = read_text("Password: ")

    # CLASS METHOD: create_student() builds and returns the Student object.
    student1 = Student.create_student(student_id, name, age, username, password)
    students.append(student1)                        # OBJECT stored in a LIST

    print("-" * 40)
    print("Student registration successful.")
    return student1


def login_student(students):
    """Check the login details and return the Student object, or None."""
    print("\n" + "=" * 40)
    print("LOGIN")
    print("-" * 40)

    username = read_text("Username: ")
    password = read_text("Password: ")

    student = find_student(students, username)
    if student is not None and student.login(username, password):
        print("Login successful.")
        print("-" * 40)
        return student

    print("Invalid username or password.")
    print("-" * 40)
    return None


def register_module_for_student(student, modules, registrations):
    """Create a Registration object that links the student to a module."""
    print("\n" + "=" * 40)
    print("MODULE REGISTRATION")
    print("-" * 40)

    module_code = read_text("Enter module code to register: ")

    # Step 1: the module must exist in the modules list.
    module1 = find_module(modules, module_code)
    if module1 is None:
        print("Module not found.")
        print("=" * 40)
        return

    # Step 2: the student must not have this module already.
    for registered in student.registered_modules:
        if registered.module_code == module1.module_code:
            print("You are already registered for this module.")
            print("=" * 40)
            return

    # Step 3: store the module in the student's list.
    student.register_module(module1)

    # Step 4: create a Registration object (object interaction) and store it.
    registration1 = Registration(student, module1)
    registrations.append(registration1)

    print("Successfully registered for:")
    registration1.display_registration()


def student_menu(student, modules, registrations):
    """Show the student menu after a successful login."""
    while True:
        print("\n" + "=" * 40)
        print("STUDENT MENU")
        print("-" * 40)
        print("1. View Student Information")
        print("2. View Available Modules")
        print("3. Register for Module")
        print("4. View Registered Modules")
        print("5. Logout")
        print("=" * 40)

        choice = read_choice("Enter your choice: ", ["1", "2", "3", "4", "5"])

        if choice == "1":
            student.display_info()                    # INSTANCE METHOD
        elif choice == "2":
            display_available_modules(modules)        # loops over Module objects
        elif choice == "3":
            register_module_for_student(student, modules, registrations)
        elif choice == "4":
            display_registered_modules(student)        # loops over Module objects
        else:
            print("Logout successful.")
            return


def main():
    """Entry point of the program."""
    students = []         # LIST of Student objects
    modules = create_available_modules()   # LIST of Module objects
    registrations = []    # LIST of Registration objects

    while True:
        print("\n" + "=" * 40)
        print("STUDENT REGISTRATION SYSTEM")
        print("-" * 40)
        print("1. Register Student")
        print("2. Login")
        print("3. Exit")
        print("=" * 40)

        choice = read_choice("Enter your choice: ", ["1", "2", "3"])

        if choice == "1":
            register_student(students)
        elif choice == "2":
            if len(students) == 0:
                print("No student has registered yet. Please register first.")
                continue
            student = login_student(students)
            if student is not None:
                student_menu(student, modules, registrations)
        else:
            print("Goodbye. Thank you for using the Student Registration System.")
            print("All data has been cleared because the program is closing.")
            break


if __name__ == "__main__":
    main()