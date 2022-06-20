# Student Grades
# Student class example with method __init__ to initialize attributes
# and __str__ to return the results with a string format

class Student:
    name: str
    grade: int
    _is_approved: bool = False

    def __int__(self, name, grade):
        self.name = name
        self.grade = grade

    def is_approved(self):
        if self.grade >= 70:
            self._is_approved: True
            return 'Approved'
        else:
            return 'Rejected'

    def __str__(self):
        return f'{self.name.capitalize()} is {self.is_approved()}'


student = Student()
student.__int__('Carlos', 70)
print(student)
