# todo_list.py

def display_todos(todos):
    print("\nTo-Do List:")
    for index, todo in enumerate(todos, start=1):
        print(f"{index}. {todo}")
    print("\n")

def add_todo(todos):
    todo = input("Enter a new to-do item: ")
    todos.append(todo)
    print(f'"{todo}" has been added to your to-do list.\n')

def remove_todo(todos):
    display_todos(todos)
    try:
        index = int(input("Enter the number of the to-do item to remove: ")) - 1
        if 0 <= index < len(todos):
            removed = todos.pop(index)
            print(f'"{removed}" has been removed from your to-do list.\n')
        else:
            print("Invalid index. Please try again.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    todos = []
    while True:
        print("1. Display To-Do List")
        print("2. Add To-Do Item")
        print("3. Remove To-Do Item")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            display_todos(todos)
        elif choice == '2':
            add_todo(todos)
        elif choice == '3':
            remove_todo(todos)
        elif choice == '4':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please choose again.\n")

if __name__ == "__main__":
    main()
