class Student:
    def __init__(self, name, group, gpa):
        self.__name = name          
        self.__group = group        
        self.__gpa = gpa            

    def get_name(self):
        return self.__name

    def get_group(self):
        return self.__group

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, new_gpa):
        if 0 <= new_gpa <= 4:
            self.__gpa = new_gpa
        else:
            print("Ошибка: GPA должен быть от 0 до 4.")

    def display_info(self):
        print(f"Имя: {self.__name}, Группа: {self.__group}, GPA: {self.__gpa}")

    def update_gpa(self, new_gpa):
        self.set_gpa(new_gpa)


class Group:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, name):
        for s in self.students:
            if s.get_name() == name:
                self.students.remove(s)
                print(f"Студент {name} удалён.")
                return
        print("Ошибка: студент не найден.")

    def show_all(self):
        print("\nСписок студентов:")
        for s in self.students:
            s.display_info()
        print()

    def get_top_students(self, threshold):
        print(f"\nСтуденты с GPA выше {threshold}:")
        for s in self.students:
            if s.get_gpa() > threshold:
                s.display_info()


if __name__ == "__main__":

    s1 = Student("Абзал", "IS-24-22", 3.5)
    s2 = Student("Ержан", "IS-24-22", 3.9)
    s3 = Student("Альмири", "IS-24-22", 2.8)

  
    group = Group()


    group.add_student(s1)
    group.add_student(s2)
    group.add_student(s3)

    group.show_all()

   
    s3.update_gpa(3.1)

    group.get_top_students(3.0)

    
    group.remove_student("Ержан")

    
    group.show_all()
