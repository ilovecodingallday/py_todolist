class TodoList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, index):
        if index >= 0 and index < len(self.items):
            del self.items[index]
        else:
            print("Invalid index")

    def print_list(self):
        if len(self.items) == 0:
            print("Todo list is empty")
        else:
            for i, item in enumerate(self.items, start=1):
                print(f"{i}. {item}")


todo_list = TodoList()

while True:
    action = input("Enter 'add' to add an item, 'remove' to remove an item, or 'print' to print the list: ")
    if action == "add":
        item = input("Enter the item you want to add: ")
        todo_list.add_item(item)
    elif action == "remove":
        for (i, item) in enumerate(todo_list.items, start=1):
            print(f"{i}. {item}")
        index = int(input("Enter the index of the item you want to remove: ")) - 1
        todo_list.remove_item(index)
    elif action == "print":
        todo_list.print_list()
    else:
        print("Invalid input, please try again.")
