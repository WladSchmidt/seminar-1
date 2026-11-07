# letter = input("Please enter a letter: ")
# if len(letter) == 1:
#     print(f"ASCII: {ord(letter)}")
# else:
#     print("Enter one character.")

# ______________________x_________________________

# def greet_user():
#     name = input("Please enter your name: ")
#     print(f"Hello, {name}.")

# greet_user()

# ______________________x_________________________

# def escape_by(plan):
#     print("Plan:", plan)

# escape_by("Jumping over")
# escape_by("Cross bridge ahead")

# ______________________x_________________________

def cross_bridge(distance):
    for step in range(distance):
        print("Crossed setep.")
    if distance > 5:
        print("The bridge is collapsing!")
    else:
        print("We must keep going")

cross_bridge(3)



