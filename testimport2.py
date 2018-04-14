from py_mod.folder_mod import MessageUser, make_messages

obj = MessageUser()
obj.add_user("Justin", 123.32)
obj.add_user("john", 94.23)
print(obj.get_details())
print(obj.make_messages)

default_names = ["Justin", "john", "Emilee", "Jim", "Ron", "Sandra", "veronica", "Whitney"]
default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]


make_messages(default_names, default_amounts)