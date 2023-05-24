class Student:
    def __init__(self, name, starting_grade=0):
        self.__name = name
        self.grade = starting_grade

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, new_grade):
        try:
            new_grade = int(new_grade)
        except(TypeError, ValueError) as e:
            raise type(e)('New grade: ' + str(new_grade) + ', is an invalid type.')
        if(new_grade < 0) or (new_grade > 100):
            raise ValueError('New grade: ' + str(new_grade) + ', must be between 0 and 100.')
        self.__grade = new_grade


oStudent1 = Student('Joe Schmo')
oStudent2 = Student('Jane Smith')

print(oStudent1.grade)
print(oStudent2.grade)
print()

oStudent1.grade = 85
oStudent2.grade = 92

# oStudent1.grade = 'abc'

print(oStudent1.grade)
print(oStudent2.grade)
