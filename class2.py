import datetime

class MessageUser():
  user_details = []
  messages = []
  base_message = """Hi {name}! 
Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!
Team CFE
"""
  def add_user(self, name, amount):
    amount = "%.2f"%(amount)
    detail = {
      "name": name,
      "amount": amount 
    }
    today = datetime.date.today()
    date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
    detail['date'] = date_text
    self.user_details.append(detail)

  def get_details(self):
    return self.user_details

  def make_messages(self):
    if len(self.user_details) > 0:
      for detail in self.get_details():
        name = detail["name"]
        amount = "%.2f"%(detail["amount"])
        date = detail["date"]
        message = self.base_message
        new_msg = base_message.format(
          name = name,
          date = date,
          total = amount
        )
        self.messages.append(new_msg)
      return self.messages
    return []

default_names = ["Justin", "john", "Emilee", "Jim", "Ron", "Sandra", "veronica", "Whitney"]
default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]

obj = MessageUser()
obj.add_user("Justin", 123.32)
obj.add_user("john", 94.23)
print(obj.get_details())
print(obj.make_messages)

# make_messages(default_names, default_amounts)