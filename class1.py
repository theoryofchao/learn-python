class Animal():
  name = 'Default'
  noise = "Grunt"
  size = "Large"
  color = "Brown"
  hair = "Covers Body"
  def get_color(self):
    return self.color
  def make_noise(self, abc):
    print(abc)
    return self.noise

## Inherit Animal
class Dog(Animal):
  name = 'Jon' ## override
  # color = 'brown'

  def get_color(self):
    return self.color

  @property ## converts a method into a property so me don't need parentheses to run it
  def print_name(self):
    print(self.name + 'print_name')

dawg = Dog()

print(dawg.make_noise('test')) ## inherited function from Animal
print(dawg.name)
dawg.print_name

def some_func(arg1=None, arg2=None, kwarg1=None, kwarg2="abc"):

  if kwarg1 != None:
    print(kwarg1)
  pass

some_func("abc", "def", kwarg1="huehue")


email_address = 'theoryofchao@gmail.com'
to_list = ['to1@gmail.com, to2@gmail.com']
from_list = ['from1@gmail.com, from2@gmail.com']

def send_email(email=email_address, to_list=to_list, from_list=from_list):
  pass