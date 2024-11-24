user_prompt = "Enter todo: "

todo1 = input(user_prompt)
length1 = len(todo1)
print("The length of the entered todo was", length1)

todo2 = input(user_prompt)
length2 = len(todo2)
print("The length of the entered todo was", length2)

todo3 = input(user_prompt)
length3 = len(todo3)
print("The length of the entered todo was", length3)

todos = [todo1, todo2, todo3]
print(todos)
total_length = length1 + length2 + length3
print("The total length of all entered todos is", total_length)

print("Type of the user_prompt: " + str(type(user_prompt)))
print("Type of the todo1: " + str(type(todo1)))
print("Type of the todos: " + str(type(todos)))
