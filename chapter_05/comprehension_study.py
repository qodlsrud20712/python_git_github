# square =[]
#
# for i in numbers:
#     square.append(i**2)
#
# print(square)  밑과 동일 한 줄에 줄일 수 있다

numbers = [1, 2, 3, 4, 5]
square = [i ** 2 for i in numbers]
print(square)


# square =[]
#
# for i in numbers:
#      if i>= 3:
#          square.append(i**2)
#
# print(square)  밑과 동일 한 줄에 줄일 수 있다

square = [i ** 2 for i in numbers if i>=3]
print(square)
