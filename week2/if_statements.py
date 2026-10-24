#First part - TASK 1

book_type = input("What type of book is this? ").strip().capitalize()

if book_type == "Adventure":
    print("\nI like adventure books!")

print("\nFinished reading book!")

# Second part - TASK 2

print("\nPlease enter the activity to be performed.")

activity = input()

if activity == "calculate":
    print("Performing calculations...")
else:
    print("Performing activity...")
    
print("Activity completed!")
