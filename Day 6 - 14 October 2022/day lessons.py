Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
input = 2
score = input * 3
print(score)
6
#simple calculation above
#changing value
input = 5
print(score)
6
#needs to be
>>> input = 5
>>> score = input * 3
>>> print(score)
15
>>> #interger
>>> pets = 2
>>> print(pets)
2
>>> #float
>>> temp = 37.5
>>> print(temp)
37.5
>>> #Combining strings HB
>>> happy = "happy birthday to you "
>>> name = "Emma "
>>> song = happy + happy + "happy \ birthday dear " + name + happy
>>> song
'happy birthday to you happy birthday to you happy \\ birthday dear Emma happy birthday to you '
>>> 
>>> #casting -change data type
>>> age = 25
>>> print("Your age is " + str(age))
Your age is 25
>>> #changed interger to string
>>> 
>>> #len tells you the length of string or list
>>> len("Hello Alan")
10
>>> 
>>> #lists
>>> my_list = {1, "two", 3, 5, 7, 4}
>>> my_list = [1, "two", 3, 5, 7, 4]
>>> my_list
[1, 'two', 3, 5, 7, 4]
>>> # \ allows you to write over two lines
>>> 
>>> my_list{0}
SyntaxError: invalid syntax
