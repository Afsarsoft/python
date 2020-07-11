# pyright: strict

#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  input(), allowing user input
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
name: str = str(input('Enter your name: '))
age: int = int(input('Enter your age: '))
print(f'Hello {name}! You are {age}')
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# simple calculator
num1: float = float(input('Enter a number: '))
num2: float = float(input('Enter another number: '))
result: float = num1 + num2

print(f'The total is {result}')
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
color: str = str(input('Enter a color: '))
noun: str = str(input('Enter a noun: '))
celebrity: str = str(input('Enter a celebrity: '))

print(f'Roses are {color}')
print(f'{noun} is blue')
print(f'I love {celebrity}')
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
weight_lbs: float = float(input('Enter your weight in pounds: '))
weight_kg: float = weight_lbs * 0.45
print(f'You are {weight_kg} Kg')
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
weight: float = float(input('Enter your weight: '))
unit: str = str(input('Enter L for pounds or K for Kilos: '))
if unit.upper() == 'L':
    converted: float = weight * 0.45
    print(f'You are {converted} kilos')
else:
    converted: float = weight / 0.45
    print(f'You are {converted} pounds')
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
answer = input('Enter a number: ')
try:
    ival = int(answer)
except:
    ival = -1

if ival > 0:
    print('Nice work')
else:
    print(f'{answer} is not a number!')
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
while True:
    answer: str = str(
        input('Please type and press Enter, to end type done ->'))

    if answer == 'done':
        break
    print(f'you typed ->{answer}')

print('done!')
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
num1: float = float(input('Enter first number: '))
num2: float = float(input('Enter second number: '))
op: str = str(input('Enter operator: '))

if op == '+':
    print(f'{num1} + {num2} = ', num1 + num2)
elif op == '-':
    print(f'{num1} - {num2} = ', num1 - num2)
elif op == '/':
    print(f'{num1} / {num2} = ', num1 / num2)
elif op == '*':
    print(f'{num1} * {num2} = ', num1 * num2)
else:
    print('Invalid operator, only +, -, /, * are acceptable')
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Guess a number
secret_number: int = 9
guess_count: int = 0
guess_limit: int = 3

while guess_count < guess_limit:
    guess: int = int(input('Guess a number: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('Sorry, you failed!')

#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Secret game
secret_word: str = "horse"
guess_word: str = ""

while guess_word != secret_word:
    guess_word = str(input("Enter an animal name: "))

print("You win!")
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Secret game, better
secret_word: str = "horse"
guess_word: str = ""
count = 0
limit = 3
expired = False

while guess_word != secret_word and not(expired):
    if count < limit:
        guess_word = str(input("Enter guess: "))
        count += 1
    else:
        expired = True

if expired:
    print("Out of guesses, YOU LOSE!")
else:
    print("You win!")
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Car game
command: str = ""
started: bool = False

while True:
    command = str(input("> ").lower())
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")

    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")

    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit
        """)

    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that!")

print("Game is completed:)")
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Creating our own language


def translate(phrase: str):
    result = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.lower():
                result = result + "G"
            else:
                result = result + "g"
        else:
            result = result + letter
    return result


print(translate(input("Enter a phrase: ")))
