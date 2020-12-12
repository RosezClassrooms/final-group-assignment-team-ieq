[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=343882&assignment_repo_type=GroupAssignmentRepo)
# Group-Assignment
This is the final group assignment for the semester. For this assignment you are required to use two design patterns that were covered post midterm.

They can be used in two separate problems, on using each, or in the same problem that require both.

Please select a problem/problems that are manageable with regards to successful implementation.

######## Edit

    As described above, I have chosen to implement two design patterns separately.
For the first one (UniversityFaculty.py), I have chosen Composite design pattern. In Composite design patterns there are a Component, Leaf,
Composition.
    Since Composite design structure is best used in part-whole structures (tree) that indicates a "has" relationship, I thought it
would be best to implement the design in universities hierarchy structure. A university has departments and these departments have
their duties. Generally, they share their duties such as planning the semester and courses, organizing the faculty
members and such. Because of their similar duties and wanting the code to be DRY, Composite design pattern is the best fit.
They still have the similar tasks(nodes) while, the composition part gives a bit freedom to adapt the code for the
requirements.
    Using an Interface to define shared tasks of departments while customizing the Composition part makes the code
efficient, organized and readable.


The second one is about the Template Design Pattern. I chose two similar concepts to have some common tasks as well as
different ones. Since it is a recent event, I chose Health sector and as classes created Doctor and Nurse.
While taking care of the patients, doctors and nurses follow similar procedures. Thus for the similar ones I have
created concrete methods and for the ones that change I created abstract methods. This project implements steps taken
for doctors and nurses in a simple manner.

