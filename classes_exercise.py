# Basic class exercise

class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  
  def add_grade(self, grade):
    if type(grade) == Grade:
      self.grades.append(grade)
    else:
      None

roger = Student('Roger van der Weyden', 10)
sandro = Student('Sandro Botticelli', 12)
pieter = Student('Pieter Bruegel the Elder', 8)

class Grade:
  minimum_passing = 65

  def __init__(self, score):
    self.score = score

pieter_grade_1 = Grade(100)
pieter.add_grade(pieter_grade_1)
