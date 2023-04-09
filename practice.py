#my fast exercise:

# count=0
# for i in range(1,21):
#     if i%2==0:
#         print(i)
#     count+=1
# print(f'we have total number is {count}')

# my second exercise:

# name=['a','e','i','f','se']
# for i in enumerate(name):
#       print(i[0])

#same as others way:

letter=['a','b','c','d']
for i in enumerate(letter):
   print(i)
# now got it:
count=0
for i in range(1,10):
   if i%2==0:
     print(i)
     count+=1
print(f'total even numbers is {count}')

#now its time to review time:
# name=['a','b','c','e','s','s','y']
# for index,i in enumerate(name):
#    print(index,i)

#next practice::

name=['a','b','c','d','e']
for index,i in enumerate(name):
   print(index,i)