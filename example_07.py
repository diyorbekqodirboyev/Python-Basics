class Student:
  def __init__(self, first_name, last_name, age):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
  def get_first_name(self):
    return self.first_name.title()
  def get_last_name(self):
    return self.last_name.title()
  def get_age(self):
    return self.age
student_1 = Student(first_name = 'Diyorbek', 'Qodirboyev')
print(student_1.get_first_name())
print(student_1.get_last_name())
print(student_1.get_age())
