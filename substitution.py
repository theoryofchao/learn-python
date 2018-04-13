import datetime

text = "this is a {variable_a} formatted string".format(variable_a = "variable based")
print(text)

text = "My name is {name}"
print(text)
print(text.format(name="TheoryOfChao"))

text = "This is argument {0}".format("0")
print(text)

text = "hi there %s! Thanks %s. %%s escapes"%("TheoryOfChao", "guy")
print(text)

## string substitution with float

text = "2 decimal place: %.2f" %(20)
print(text)

text = "10 decimal place: %.10f" %(20)
print(text)

text = "400 decimal place: %.400f" %(20)
print(text)

datetime_now = datetime.datetime.now()
datetime_today = datetime.date.today()