class student:
    def __init__(self, name, group, grades, tel_number):
        self.name = name
        self.group = group
        self.grades = grades
        self.__tel_number = tel_number

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def info(self):
        print(f"имя: {self.name}, группа: {self.group}, оценки: {self.grades}, средний балл: {self.get_average():.2f}, телефон: {self.__tel_number}")

student1 = student("Леша", "46-71", [3, 5, 4], "+79521112733")
student2 = student("Марк", "25-46", [5, 5, 5], "+79674845566")
student3 = student("Азалия", "36-51", [4, 5, 5], "+79226778899")

student1.add_grade(5)
student2.add_grade(4)
student3.add_grade(5)

student1.info()
student2.info()
student3.info()