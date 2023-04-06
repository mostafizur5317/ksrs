command=" hello"
while command.lower() !="quit":
    command=input(">")
    if command.lower()=="start":
        print("car stated...")
    elif command.lower()=="stop":
        print("car started")
    elif command=='help':
        print("""
        start-to start the car
        stop-to stop the car
        quit- to quit
        """)
    else:print('sorry i dont understant')
