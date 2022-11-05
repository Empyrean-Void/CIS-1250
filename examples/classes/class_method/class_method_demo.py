class Student:
    name = ''
    student_number = None
    __gpa = None
    classes = []

    def set_gpa(self, gpa):
        if 0 <= gpa <= 5:
            self.__gpa = gpa
        else:
            self.gpa = None

    def get_gpa(self):
        return self.__gpa

    def display_student_info(self):
        return f'{self.name} {self.student_number} {self.__gpa}'


if __name__ == "__main__":
    new_student = Student()

    new_student.name = input('Enter name: ')
    new_student.student_number = int(input('Enter student ID number: '))
    new_student.set_gpa(float(input('Enter student GPA: ')))
    new_student.classes = ['CIS-1250', 'CIS-1680']

    print(new_student.display_student_info())
