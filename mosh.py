cool=""
started=False
while True:
    cool=input(">").lower()

    if cool=='start':
        if started:
            print("car already started")
        else:
            started=True
            print('car start')
    elif cool=='stop':
        if started :
            print('car already stoped')
        else:
            started=False
            print("car stop")

    elif cool=='help':
         print("help not availavil")
    else:print('i dont undrstant')