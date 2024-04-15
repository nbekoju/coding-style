"""
assignment for OOP
"""

# Create a Python class to represent a University.
# The university should have attributes like name, location, and a list of departments.
# Implement encapsulation to protect the internal data of the University class.
# Create a Department class that inherits from the University class.
# The Department class should have attributes like department name,
# head of the department, and a list of courses offered.
# Implement polymorphism by defining a common method for both the University
# and Department classes to display their details.


class University:
    """
    Represents a University.

    Attributes:
        name (str): The name of the university.
        location (str): The location of the university.
        departments (list): A list of departments in the university.
    """

    def __init__(self, name, location):
        self.__name = name
        self.__location = location
        self.__departments = []

    def get_name(self):
        """get name of the university"""
        return self.__name

    def get_location(self):
        """get location of university"""
        return self.__location

    def add_department(self, department):
        """add department to the university"""
        self.__departments.append(department)

    def display_details(self):
        """display the details of the university"""
        print("University Name:", self.__name)
        print("Location:", self.__location)
        print("Departments:")
        for department in self.__departments:
            print("\t", department.get_name())


class Department(University):
    """
    Represents a department

    Attributes:
        university, location, name, hod
    """

    def __init__(self, university, location, name, hod):
        super().__init__(university, location)
        self.__name = name
        self.__hod = hod
        self.__courses_offered = []

    def __str__(self) -> str:
        """return the name of department in print statement"""
        return self.__name

    def get_name(self):
        """return the name of department"""
        return self.__name

    def get_head(self):
        """get the hod of department"""
        return self.__hod

    def add_course(self, course):
        """add new course to the department"""
        self.__courses_offered.append(course)

    def display_details(self):
        """print the details of the department"""
        print("Department Name:", self.__name)
        print("Head of Department:", self.__hod)
        print("Courses Offered:", self.__courses_offered)


if __name__ == "__main__":
    uni = University("Tribhuwan University", "Kirtipur")

    dept1 = Department(
        "Tribhuwan University", "Kirtipur", "Computer Engineering", "Hari"
    )
    dept1.add_course("Artificial Intelligence")
    dept1.add_course("Data Structures and Algorithms")
    uni.add_department(dept1)

    dept2 = Department("Tribhuwan University", "Kirtipur", "Civil Enginerering", "Ram")
    dept2.add_course("Hydraulics")
    dept2.add_course("Applied Mechanics")
    uni.add_department(dept2)

    uni.display_details()
    print("\n")
    dept1.display_details()
    print("\n")
    dept2.display_details()
