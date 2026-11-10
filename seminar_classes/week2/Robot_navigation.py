# If statements task (Robot Navigation)

print('--- Welcome to Robot Navigation --- ')

direction = input('\nWhich direction should I go? (up, down, left or right)? ').strip().lower()

if direction == 'up':
    print('\nI am moving in an upward direction!')

elif direction == 'down':
    print('\nI am moving in a downward direction!')

elif direction == 'left':
    print('\nI am moving left!')

elif direction == 'right':
    print('\nI am moving right!')

else:
    print('\nUnknown direction!')

