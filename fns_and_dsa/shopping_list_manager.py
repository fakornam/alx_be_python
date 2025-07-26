def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
def add_item(shopping_list):
    item = input("Enter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to your shopping list")
    else:
        print("Item cannot be empty")
        
def remove_item(shopping_list):
    item = input(f"Enter the item to be removed: ").strip()
    if item:
        shopping_list.remove(item)
        print(f"'{item}'item has been removed")
    else: 
        print(f"'{item}' not found in shopping_list")

def view_item(shopping_list):
    print("\n Your Shopping List:")
    if shopping_list:
        for i, item in enumerate(shopping_list, start=1):
          print(f"{i}. {item}")
        else:
          print("Your shopping list is empty.")
          
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_item(shopping_list)
        elif choice == '4':
            print("Exiting Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 4.")

if __name__ == "__main__":
    main()
        

    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
