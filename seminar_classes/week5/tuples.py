# group1 = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
# alcalines = tuple(group1)
# print(type(alcalines))

# print(sorted(alcalines))
# print(alcalines)

# __________________X_________________

# def steps():
#     likelihoods = [
#         ("step 1", 50),
#         ("step 2", 38),
#         ("step 3", 27),
#         ("step 4", 99),
#         ("step 5", 4)
#     ]
#     return likelihoods

# def run_task3():
#     records = steps()
#     good_steps, bad_steps = [], []
#     for step in records:
#         if step[1] >= 50:
#             bad_steps.append(step)
#         else:
#             good_steps.append(step)
#     print(f"Good steps: {len(good_steps)}, "
#           f"Bad steps: {len(bad_steps)}")

# run_task3()

# __________________X_________________

# def list_of_teachers():
#     return [("Drishty", "Course Leader"),
#             ("Darren", "Module Leader")]

# print(list_of_teachers()[1][1])
