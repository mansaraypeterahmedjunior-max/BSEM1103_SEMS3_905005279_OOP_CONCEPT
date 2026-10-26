# Student Registration, Login and Module Offering System

An Object-Oriented Programming (OOP) academic project written in Python.
It is a small console application that demonstrates how classes, objects,
instance methods, class methods, static methods, object interaction and list
data structures can be used to model a simple university student registration
process.

---

## 1. Project Title

**Student Registration, Login and Module Offering System**

## 2. Introduction

This project is a terminal-based Python program for university students. A
student can register an account, log in, view the academic modules offered by
the university, register for modules and view the modules already registered.

The program uses only the Python standard library and runs completely in the
terminal. It was written for an OOP assignment, so the code is deliberately
simple and easy to explain during an oral presentation.

## 3. Problem Statement

Manual university registration can lead to:

- Incorrect or incomplete student information.
- Difficulty keeping student records organised.
- Duplicate registration of students and modules.
- Difficulty tracking the modules a student has selected.
- Errors when recording a module registration.

This project demonstrates a small digital prototype that organises these
activities with Python OOP. It does **not** claim to solve all university
registration problems; it only shows how OOP can organise the process.

## 4. Proposed Solution

Build a simple Python console application where a student can:

1. Create a student account.
2. Enter student information using `input()`.
3. Create a username and password.
4. Log into the system.
5. View available modules.
6. Select and register for modules.
7. View registered modules.
8. Log out.

The main entities of the process are represented by Python classes and objects.

## 5. Project Objectives

- Demonstrate classes, objects, attributes and instance methods.
- Demonstrate a class method and a static method.
- Demonstrate object interaction between different classes.
- Use Python lists as the main data structure.
- Practise user input with `input()` and basic validation.
- Practise student registration, login and module registration logic.

## 6. Institutional Context

- **Domain:** Education.
- **Country:** Sierra Leone.
- **Institution:** University student registration and academic module
  management.
- **Scope:** An academic prototype, not a production university management
  system.

## 7. OOP Concepts Used

| Concept | Where it appears |
| --- | --- |
| Class | `Student`, `Module`, `Registration` |
| Object | `student1`, `module1`, `registration1` |
| Attributes | `student_id`, `name`, `module_code`, `credit_units`, `student`, `module` |
| Constructor | `__init__()` in every class |
| Instance method | `display_info()`, `login()`, `register_module()`, `display_module()`, `display_registration()` |
| Class method | `Student.create_student()` |
| Static method | `Student.validate_age()` |
| Object interaction | `Registration(student1, module1)` |
| List data structure | `students`, `modules`, `registrations` |
| User input | `input()` used for every user value |
| Validation | name, age, student ID, username, password, module code |

## 8. Student Class (`student.py`)

The `Student` class stores student information and student behaviour.

```python
class Student:
    MIN_AGE = 15
    MAX_AGE = 100

    def __init__(self, student_id, name, age, username, password):
        ...
```

`main.py` creates a Student object through the class method:

```python
student1 = Student.create_student(student_id, name, age, username, password)
students.append(student1)
```

## 9. Module Class (`module.py`)

The `Module` class represents a module offered by the university.

```python
module1 = Module("CS101", "Introduction to Programming", 3)
```

| Code | Module name | Credits |
| --- | --- | --- |
| CS101 | Introduction to Programming | 3 |
| CS102 | Database Systems | 3 |
| SE201 | Object-Oriented Programming | 3 |
| SE202 | Web Development | 3 |
| SE203 | Computer Networks | 3 |

This module data is fictional and used for demonstration only.

## 10. Registration Class (`registration.py`)

The `Registration` class represents the relationship between a student and a
module. It must receive a `Student` object and a `Module` object.

```python
registration1 = Registration(student1, module1)
```

## 11. Attributes

**Student:** `student_id`, `name`, `age`, `username`, `password`,
`registered_modules`

**Module:** `module_code`, `module_name`, `credit_units`

**Registration:** `student`, `module`

## 12. Instance Methods

| Method | Class | What it does |
| --- | --- | --- |
| `display_info()` | Student | Prints the student's information |
| `login()` | Student | Checks a username and password |
| `register_module()` | Student | Adds a module to `registered_modules` |
| `display_module()` | Module | Prints one module in a readable line |
| `display_registration()` | Registration | Prints the student and the module |

## 13. Class Method

```python
@classmethod
def create_student(cls, student_id, name, age, username, password):
    student = cls(student_id, name, age, username, password)
    return student
```

The class method receives the class (`cls`) as its first argument and returns a
new `Student` object.

## 14. Static Method

```python
@staticmethod
def validate_age(age):
    return Student.MIN_AGE <= age <= Student.MAX_AGE
```

The static method does not need the class or the object; it only checks whether
an age is between 15 and 100.

## 15. Object Interaction

`Registration` holds a `Student` object and a `Module` object. It uses the
Student object to read the student's name and ID, and it asks the Module object
to display itself. This is the clearest example of objects of different classes
working together:

```python
registration1 = Registration(student1, module1)
registration1.display_registration()
```

## 16. List Data Structures

Plain Python lists are the only storage mechanism:

```python
students = []
modules = []
registrations = []
```

Objects are appended to the lists and the lists are searched with simple
`for` loops. No databases, dictionaries or sets are used.

## 17. Student Registration Process

1. User selects `1. Register Student` from the main menu.
2. The program asks for Student ID, Name, Age, Username and Password using
   `input()`.
3. Each value is validated; invalid values ask the user to try again.
4. `Student.create_student()` builds the Student object.
5. The object is appended to `students`.
6. `Student registration successful.` is displayed.

## 18. Login Process

1. User selects `2. Login`.
2. The program asks for the username and password.
3. The `students` list is searched for a matching username.
4. If the username and password match, `Login successful.` is displayed and the
   student menu appears.
5. Otherwise `Invalid username or password.` is displayed.

No encryption, tokens or advanced authentication are used.

## 19. Module Offering

`create_available_modules()` creates the list of `Module` objects offered by
the university. `display_available_modules()` loops through the list and prints
each module:

```
========================================
AVAILABLE MODULES
----------------------------------------
1. CS101 | Introduction to Programming | 3 Credits
2. CS102 | Database Systems | 3 Credits
3. SE201 | Object-Oriented Programming | 3 Credits
4. SE202 | Web Development | 3 Credits
5. SE203 | Computer Networks | 3 Credits
========================================
```

## 20. Module Registration

The student enters a module code, for example `SE201`. The program:

1. Checks whether the module exists in the modules list (`Module not found.` if
   it does not).
2. Checks whether the student already registered for it (`You are already
   registered for this module.`).
3. Adds the Module object to the student's `registered_modules` list.
4. Creates a `Registration` object and appends it to `registrations`.
5. Displays the successful registration.

## 21. Input Validation

| Field | Rule |
| --- | --- |
| Student ID | Must be text and must not already be registered (e.g. `ST001`) |
| Name | Must contain letters, cannot be empty, numbers-only names rejected |
| Age | Must be a whole number between 15 and 100 (letters and decimals rejected) |
| Username | Must not be empty and must be unique |
| Password | Must not be empty |
| Menu choice | Must be one of the options shown |
| Module code | Must exist in the modules list and must not be registered twice |

## 22. How to Run the Program

Requirements: Python 3 installed. No external packages are needed.

```bash
python main.py
```

(On Windows the launcher may be used: `py main.py`)

The program must be run from the project folder so that it can find
`student.py`, `module.py` and `registration.py`.

## 23. Example Output

```
========================================
STUDENT REGISTRATION SYSTEM
----------------------------------------
1. Register Student
2. Login
3. Exit
========================================
Enter your choice: 1
========================================
STUDENT REGISTRATION
----------------------------------------
Student ID: ST001
Name: Mohamed
Age: 20
Username: mohamed01
Password: python123
----------------------------------------
Student registration successful.

========================================
STUDENT REGISTRATION SYSTEM
----------------------------------------
1. Register Student
2. Login
3. Exit
========================================
Enter your choice: 2
========================================
LOGIN
----------------------------------------
Username: mohamed01
Password: python123
Login successful.
----------------------------------------

========================================
STUDENT MENU
----------------------------------------
1. View Student Information
2. View Available Modules
3. Register for Module
4. View Registered Modules
5. Logout
========================================
Enter your choice: 3
========================================
MODULE REGISTRATION
----------------------------------------
Enter module code to register: SE201
Successfully registered for:
========================================
MODULE REGISTRATION
----------------------------------------
Student: Mohamed ( ST001 )
SE201 | Object-Oriented Programming | 3 Credits
========================================
```

## 24. DPG Principles

This project is **not** an officially certified Digital Public Good. It is a
student project designed to align with relevant DPG principles.

1. **Open Source** — the source code can be published on GitHub for
   educational use so that other students can learn from it.
2. **Inclusive and Accessible** — the application runs in a plain terminal
   using standard Python. It does not need expensive hardware, a database
   server or specialised software, so it can be used on low-cost devices.
3. **Privacy-Respecting** — only fictional student information is used.
   Passwords exist only to demonstrate a basic login function. This is
   **not** a production authentication system.
4. **Modular and Reusable** — `Student`, `Module` and `Registration` are in
   separate Python files. The classes can be imported and extended in future
   educational projects.

## 25. Privacy Considerations

- Only fictional data should be used in the demonstration.
- No real student records are stored by this prototype.
- No real passwords should be used; use made-up demonstration passwords.
- The application has no database and no file storage.
- Data exists only in Python lists while the program is running and is lost
  when the program closes.
- This prototype must not be used for real university student records.

## 26. Limitations

- Data is stored only in Python lists.
- All data disappears when the program is closed.
- There is no database.
- Authentication is basic and educational.
- There is no password encryption and passwords are stored as plain text.
- There is no administrator account, no lecturer view and no reporting.
- There is no real university integration.
- There is no online access; the program is offline only.
- There is no production security of any kind.
- Module capacity, prerequisites, grades and fees are not modelled.

## 27. Project Structure

```
Student-Registration-System/
│
├── main.py          # Entry point: menus, input, validation, lists
├── student.py       # Student class
├── module.py        # Module class
├── registration.py  # Registration class
├── README.md        # Project documentation
└── screenshots/     # Terminal screenshots of the running program
```

## 28. Conclusion

This project shows how a small amount of clear Python OOP code can organise a
real process. Classes (`Student`, `Module`, `Registration`) describe the
entities, objects hold the data, instance methods give the objects behaviour, a
class method and a static method show the other two method types, and lists
keep everything together. Adding login, validation and module registration
turns the classes into a working console prototype that is simple enough to
explain line by line and small enough to extend later.

---

**Note:** This is an academic prototype for an OOP assignment. It is not a
production university registration system.# BSEM1103_SEMS3_905005279_OOP_CONCEPT
