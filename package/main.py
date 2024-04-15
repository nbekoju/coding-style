from oop.q1_oop import University, Department

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