# phone=input("phone:")
# mapping={
#     '1':'one',
#     '2':'two',
#     '3':'three',
#     '4':'four',
#     '5':'five',
# }
# output=""
# for i in phone:
#     output+=mapping.get(i)+" "
# print(output)

phone=input('phone:')
fix={
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine',
}
output=""
for i in phone:
    output+=fix.get(i) + " "
print(output)