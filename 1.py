class Academicsubject:
    def __init__(self, name, teacher, number_of_hours):
        self.name = name
        self.teacher = teacher
        self.number_of_hours = number_of_hours

    def description_of_item(self):
        return f"Предмет: {self.name}, Преподаватель: {self.teacher}, Количество часов: {self.number_of_hours}"


subject = Academicsubject("Русский", "Игорь Игорьевич Игорев", 56)
print(subject.description_of_item())
