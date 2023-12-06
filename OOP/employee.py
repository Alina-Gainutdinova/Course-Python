class Employee:
    def __init__(self, name: str, position: str, salary: float):
        self.name = name
        self.position = position
        self.salary = salary

    def promote(self, percent):
        if percent < 0:
            print("Процент не может быть отрицательным")
            return
        percentage = self.salary * percent / 100
        self.salary += percentage

    def show_salary(self):
        print(f"Зарплата {self.name} ({self.position}): ${self.salary}")


employee_1 = Employee("Azamat", "CEO", 7000)
employee_1.show_salary()
employee_1.promote(-25)
employee_1.show_salary()

employee_2 = Employee("Alina", "Backend-dev", 5500)
employee_2.show_salary()
employee_2.promote(25)
employee_2.show_salary()
