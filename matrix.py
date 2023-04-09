matrix=[
    [1,2,3,45],
    [12,31,23,45],
    [43,65,67,89],
    [98,23,12,54]

]
max=matrix[0][0]
sum=0
for i in matrix:
    for num in i:
        if num >max:
            max=num
            sum+=num

print(max)
print(sum)




# matrix = [    [1, 2, 3, 12],
#     [5, 6, 7, 5],
#     [9, 6, 5, 2],
#     [3, 12, 3, 4]
# ]
#
# max_num = matrix[0][0]
# for row in matrix:
#     for num in row:
#         if num > max_num:
#             max_num = num
#
# print("Maximum number in the matrix is:", max_num)
