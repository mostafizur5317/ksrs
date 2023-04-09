numbers=[1,22,3,3,4,34,56,223,456,67]
web=[]
for i in numbers:
    if i not in web:
        web.append(i)
print(web)