# apples = int(input("How many apples should I remove? "))
# removed = 0
# while removed < apples:
#     print("Removed apple.")
#     removed += 14

#_________________________X______________________

# obstacles = int(input("How many obstacles must I avoid? "))
# count = 0
# while count < obstacles:
#     print("Avoiding...", end="")
#     count += 1
#     print(f"Done! {count} obstacles avoided.")
# print("All obstacles have been avoided")

#_________________________X______________________

# print("Calculating the sum of the first 100 numbers...")
# total = 0
# number = 1
# while number <= 100:
#     total += number
#     number += 1
# print(f"... Done! The answer is {total}.")

#_________________________X______________________

print("How many mountains should I display?")
mountains = int(input())
print("Displaying...")
for count in range(mountains):
    print('    __')
    print('   /  \\_')
    print('  /^    \\')
    print(' /  ^     \\')
    print('/_^_^____^_\\')
print("\nDone!")

