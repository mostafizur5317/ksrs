import random
mobile_list=[
    {'name':'iphone 22','price':2345},
    {'name': 'xiaomi 22', 'price': 3342},
    {'name': 'levo 22', 'price': 234},
    {'name': 'samsung 22', 'price': 5452},
    {'name': 'livio 22', 'price': 62453},
    {'name': 'tecno 22', 'price': 78432},

]
for mobile in mobile_list:
    text=[f'this is {mobile.get("name")} and this price was {mobile.get("price")}',
          f'tjpso {mobile.get("name")} and those was {mobile.get("price")}']

    print(random.choice(text))