import datetime

names = ["Justin", "john", "Emilee", "Jim", "Ron", "Sandra", "veronica", "Whitney"]
amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]

unformatted_message = """Hi {name}! 
Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was {total}.
Have a great one!
Team CFE
"""

names_length = len(names)
amounts_length = len(amounts)

total_length = names_length if names_length >= amounts_length else amounts_length

def make_messages(names, amounts):
  messages = []
  names_length = len(names)
  amounts_length = len(amounts)
  total_length = names_length if names_length >= amounts_length else amounts_length

  i = 0
  for name in names:
    new_message = unformatted_message.format(
      name = name,
      date = datetime.datetime.now(),
      total = "%.2f"%(amounts[i]) 
    )
    i+=1
    print(new_message)

make_messages(names, amounts)

BCAA
nTrust
HSBC
