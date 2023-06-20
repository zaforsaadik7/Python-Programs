def display_menu():
    print('Shopping List Menu:')
    print('1. View shopping list.')
    print('2. Add item to the shopping list.')
    print('3. Remove item from the shopping list.')
    print('4. Exit.')

def view_list(shopping_list):
    if shopping_list:
        for item in shopping_list:
            print(item)
    else:
        print('Shopping list is empty.')

def add_item(shopping_list):
    item = input('Add your item: ')
    shopping_list.append(item)
    print(item, 'is added to the list.')

def remove_item(shopping_list):
    item = input('Enter item to remove: ')
    if item in shopping_list:
        shopping_list.remove(item)
        print(item, 'is removed from the list.')
    else:
        print(item, 'is not found in the list.')

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input('Enter your choice (1-4): ')
        if choice == '1':
            view_list(shopping_list)
        elif choice == '2':
            add_item(shopping_list)
        elif choice == '3':
            remove_item(shopping_list)
        elif choice == '4':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == '__main__':
    main()
