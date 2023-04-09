command=''
started=False
while True :
    command=input(">").lower()
    if command=="start":
        if started:
          print('car already started')
        elif
          started=True
          print("car started")
    elif command=="stop":
        if started==False:
        print('car stoped')
    else:print('car already stoped')
    elif command=='help':
        print("""
        hold on we will met you soon
        """)
    else:print('i dont understant wait a minute')

