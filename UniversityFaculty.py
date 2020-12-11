# CS342 Final Project #1
# Ezgi Cakir
# Composite Design Pattern for various departments/faculties in a university

from abc import ABC, abstractmethod


class Department(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def make_announcements(self):
        pass

    @abstractmethod
    def create_syllabus(self):
        pass


class ComputerScience(Department):
    def __init__(self, update, num_course):
        self.update = update
        self.num_course = num_course

    def make_announcements(self):
        print("The Computer Science Department announces that " + self.update)

    def create_syllabus(self):
        print("The Computer Science Department currently has " + str(self.num_course) + " various courses to pick from!")
        return self.num_course

class MechanicalEngineering(Department):
    def __init__(self, update, num_course):
        self.update = update
        self.num_course = num_course

    def make_announcements(self):
        print("The Mechanical Engineering Department announces that " + self.update)

    def create_syllabus(self):
        print("The Mechanical Engineering Department currently has " + str(self.num_course) + " various courses to pick from!")
        return self.num_course

class University(Department):
    def __init__(self):
        self.departments = []

    def make_announcements(self):
        print("The Binghamton University currently has " + str(len(self.departments)) + " number of departments.")
        for dpt in self.departments:
            dpt.make_announcements()

    def create_syllabus(self):
        total = 0
        for dpt in self.departments:
            total += dpt.create_syllabus()
        print("Binghamton University has " + str(total) + " number of courses to assist its students.")

    def add_department(self, dpt):
        self.departments.append(dpt)

    def remove_department(self, dpt):
        self.departments.remove(dpt)


def main():

    computer_science = ComputerScience("due to COVID-19, the classes will be online for two weeks mandatorily.", 48)
    mechanical_eng = MechanicalEngineering("the examination period will be extended 3 more days.", 52)

    university = University()
    university.add_department(computer_science)
    university.add_department(mechanical_eng)
    university.make_announcements()
    university.create_syllabus()


if __name__ == "__main__":
    main()








