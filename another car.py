common=""
started=False
while True:
    common=input(">").lower()
    if common=="start":
        if started:
            print("car already stopped")
        else:
            started = True
            print("car start")
    elif common =='stop':
            if not started:
                print('Car is already stopped!')
            else:
                started = False
                print('Car stopped.')
    elif common=="help":
        print("hold on soon")

