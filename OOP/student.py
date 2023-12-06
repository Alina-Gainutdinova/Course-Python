class Student:
    def __init__(self, first_name, last_name, group) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.group = group

    def say_hello(self):
        print(f"Hello I'm {self.first_name} {self.last_name}.")


student1 = Student("Azamatim", "Isakov", "168-21")
student2 = Student("Alina", "Isakova", "168-21")

student1.say_hello()
student2.say_hello()
