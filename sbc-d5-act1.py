numbers = [int(input(f"Enter Number {i+1}: ")) for i in range(3)]
print(f"All entered numbers: {numbers}")

while numbers:
    user = int(input("Is the boss here? Enter 0 for No, 1 for Yes: "))
    
    if user == 0:
        numbers.pop()
    elif user == 1:
        numbers.pop(0)
    else:
        print("Invalid input. Please enter 0 for No or 1 for Yes.")
    
    print(f"Updated numbers: {numbers}")

print("No more numbers left.")
