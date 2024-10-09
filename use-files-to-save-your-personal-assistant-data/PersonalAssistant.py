class PersonalAssistant:
  # Add an __init__ function here
  def __init__(self,todos):
  # Complete the get_contact function code
    # self.contacts = {'Ann': 'Marketing Coordinator', 'Chelsea': 'Software Developer', 'Nichole': 'Sales Representative', 'Max': 'Technical Writer'}
    self.todos = todos

  def add_todo(self, new_item):
    self.todos.append(new_item)

  def remove_todo(self, todo_item):
    if todo_item in self.todos:
      # Get the todo_item index in list
      index = self.todos.index(todo_item)
      # pop the index for todo_item in todos list
      self.todos.pop(index)
    else:
      print("Todo is not in list!")
  
  def get_todos(self):
    return self.todos
  
  def get_birthday(self, name):
    if name == "Dylan":
      print ("Birthday is 07/02/89!")
    elif name == "Melisa":
      print("Birthday is 05/03/89!")
    elif name == "Elizabeth":
      print("Birthday is 06/01/2025")
    else:
      print("Can't find a birthday for this person...")

  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return "No contact with that name"

# Code to test output of the class
# assistant = PersonalAssistant()
# assistant.add_todo("Pick up groceries")
# Change name to one from your contacts
print(assistant.get_contact("Chelsea"))
print(assistant.get_todos())
print(assistant.get_birthday("Dylan"))