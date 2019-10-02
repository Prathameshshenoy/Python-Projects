import random
a = random.randint( 1,20)
i = 0
while i<6:
    b=int(input('guess: '))
    if b<a:
        print(f"the number is greater than {b}")
    elif b>a:
        print(f"the number is less than  {b}")
    elif b==a:
        print('you guessed it!')
        break
    i = i+1
print(f"THE NUMBER IS: {a}!")
