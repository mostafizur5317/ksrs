numbers=[2,23,2,3,2,23,34,53,456,23,45]
we=[]
for i in numbers:
    if i not in we:
        we.append(i)
print(we)
