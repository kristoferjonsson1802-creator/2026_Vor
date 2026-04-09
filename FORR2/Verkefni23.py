class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")
        print(f"Average Grade: {self.calculate_average():.2f}")


student1 = Student("Alice", 16, "S12345")
student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(78)
student1.display_info()

student2 = Student("Bob", 17, "S67890")
student2.add_grade(92)
student2.add_grade(88)
student2.add_grade(68)
student2.display_info()