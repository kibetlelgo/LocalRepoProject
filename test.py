class Dog:
  breed = "Kangal"

  def __init__(self, name):
    self.name = name

  @classmethod

  def change_breed(cls, new_breed):
    cls.breed = new_breed

  def show_info(self):
    print(f"{self.name} is a {self.breed}")

dog1 = Dog("Buddy")
dog1.show_info()        