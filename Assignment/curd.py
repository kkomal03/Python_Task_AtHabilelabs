import json
import os

FILE_NAME = 'data.json'
def load_users():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    else:
        return {}
def save_users(users):
    with open(FILE_NAME, 'w') as file:
        json.dump(users, file, indent=4)


def create_user(users):
    user_id = input("Enter User ID: ")
    if user_id in users:
        print("User ID already exists.")
    else:
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        users[user_id] = {"name": name, "email": email}
        save_users(users)
        print("User created successfully!")


def read_users(users):
    if not users:
        print(" No users found.")
    else:
        print("\n List of Users:")
        for uid, info in users.items():
            print(f"ID: {uid}, Name: {info['name']}, Email: {info['email']}")


def update_user(users):
    user_id = input("Enter User ID to update: ")
    if user_id in users:
        name = input("Enter new Name: ")
        email = input("Enter new Email: ")
        users[user_id] = {"name": name, "email": email}
        save_users(users)
        print("User updated successfully!")
    else:
        print("User not found.")


def delete_user(users):
    user_id = input("Enter User ID to delete: ")
    if user_id in users:
        del users[user_id]
        save_users(users)
        print("User deleted successfully!")
    else:
        print("User not found.")

# Main menu
def show_menu():
    users = load_users()
    while True:
      
        print(" JSON-Based CRUD App \n")
  
        print("1. Create User")
        print("2. View Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            create_user(users)
        elif choice == '2':
            read_users(users)
        elif choice == '3':
            update_user(users)
        elif choice == '4':
            delete_user(users)
        elif choice == '5':
            print(" Exit")
            break
        else:
            print(" Invalid choice. Please try again.")


show_menu()
