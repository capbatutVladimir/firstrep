class Animal:
  def __init__(self,name):
      self.name = name

  def listen(self,music):
      print(f'I love to listen {music}')

class Lion(Animal):
  pass


class Turtle(Animal):
    pass


lion = Lion('Bake')
turtle = Turtle('Gheorghe')
print('My name is:')
print(lion.name)
lion.listen('Rammstein')
print('My name is:')
print(turtle.name)
turtle.listen('Viktor Tsoy-Spokoinaia No4b')
a = list()
a.append(1)
print(a)