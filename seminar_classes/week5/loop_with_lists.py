# def movements():
#     path = ["Move Forward", 10, "Move Backward", 5,
#             "Move Left", 3, "Move Right", 1]
#     return path

# def run_task2():
#     print("Moving...")
#     path = movements()
#     for i in range(0, len(path), 2):
#         print(f"{path[i]} for {path[i+1]} steps")

# run_task2()
# ________________________X_______________________

# route = []
# for i in range(3):
#     route.append("Forward")

# print(route)

# ________________________X_______________________

def menu():
    options = ["Move Forward", "Move Backward", "Move Left", "Move Right"]

    while True:
        try:
            choice = int(input("Direction (0–3): "))
            if choice >= 0 and choice < len(options):
                break
            print("Choose 0, 1, 2 or 3.")
        except ValueError:
            print("Enter a number.")

    return options[choice]


print(menu())
