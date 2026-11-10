def multiplication(a, b):
    return a * b

again = 'Y'

print('--- Welcome to the simple multiplication calculator ---\n')

while again == 'Y':
    try:
        n1 = int(input('Enter your first number to multiply: '))
        n2 = int(input('Enter your second number to multiply: '))

    except ValueError:
        print('Error: Please enter numbers only.\n')
        continue

    result = multiplication(n1, n2)
    print(f'\nYour result is: {result}\n')

    again = input('Do you want to continue (Y/N): ').strip().upper()

    while again not in ('Y', 'N'):
        print('Invalid answer. Please enter only Y or N.')
        again = input('Do you want to continue (Y/N): ').strip().upper()

print('\nThanks for using our app!')