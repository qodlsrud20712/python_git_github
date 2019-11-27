from chapter_10.my_area import *
import chapter_10.my_area
from chapter_10.my_module2 import *
from chapter_10.my_module1 import *
import random


print('pi = ', PI)
print('square area = ', square_area(5))

print(dir(chapter_10.my_area))

#[print(content) for content in dir(chapter_10.my_area)]
#
# func1()
# func2()
# func3()

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
print('주사위 두개의숫자: {}, {}'.format(dice1, dice2))

print(random.randrange(0,11,2))

num1 = random.randrange(1,10,2)
num2 = random.randrange(0,100,10)
print('num1:{}, num2:{}'.format(num1, num2))

menu = ['비빔밥', '된장', '볶음밥', '불고기', '스파게티']
print(random.choice(menu))

print(random.sample([1,2,3,4,5], 2))