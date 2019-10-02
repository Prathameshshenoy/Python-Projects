car = ""
while True:
    car = input(">").lower()
    if car == "start":
        print('the car has started')
    elif car == "stop":
       print('car has stopped')
    elif car == "help":
        print("""
start = to start the car
stop = to stop the car
quit = quit the game""")
    elif car == "quit":
        print('thank you for playing')
        break
    else:
        print('i dont understand')
