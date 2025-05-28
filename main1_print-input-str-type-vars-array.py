user_prompt = "Enter todo"
todo1 = input(user_prompt + "1: ")
todo2 = input(user_prompt + "2: ")
todo3 = input(user_prompt + "3: ")

todos = [todo1, todo2, todo3]
print(todos)

# Debug
print("Type of the user_prompt: " + str(type(user_prompt)))
print("Type of the todo1: " + str(type(todo1)))
print("Type of the todos: " + str(type(todos)))
