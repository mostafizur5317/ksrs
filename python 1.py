import random

name = ['mostafizur', 'rahman', 'alex', 'livio', 'ultra', 'semual']
age = [20, 23, 24, 50, 65, 87, 98, 983]

i = 0
while i < len(name):
    wap =random.choice(name)
    paw =random.choice(age)
    sence = [
        f'hello ths mr lawri {wap} and h was in {paw}',
        f'non the less  {wap} which is mosta {paw}',
        f'everythong loooks {wap} so be care {paw}',
        f'habe ever tested mer {wap} sorrry mr lawrity {paw}',
        f'thank you mr {wap} we will me soon at {paw}',
    ]
    print(random.choice(sence))
    i+=1
