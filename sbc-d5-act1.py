list = []
while True:
        
        command = input("Enter command number: ").strip()
        
        if command == "1":
            value = input("Enter value to add: ").strip()
            list.append(value)
        
        elif command == "2":
            print(list)
        
        elif command == "3":
            if list:
                list.pop()
            else:
                print("List is already empty.")
        
        elif command == "0":
            print("Exiting program.")
            break
        
        else:
            print("Unknown command. Please use 1, 2, 3, or 0.")


 