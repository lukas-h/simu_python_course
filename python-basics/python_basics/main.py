import math

a = 1 # integer
print(a)
b = 1.5 # floating point number double precision
print(b)

add = 1 + 2
sub = 1 - 2
mul = 1 * 2
div = 1 / 2
pow = 1 ** 2
sqrt = math.sqrt(2)

def function(x):
    return x ** x

string = "Hello"
string2 = string + ", World!"
print(string2)
string3 = string2.replace('World', 'Simuuu').replace('!', ' <3')
print(string3)

if(string == 'Hello'):
    print('Hello from if statement')
else:
    print('This is never called')

array = ["foo", "bar", "baz"]
print("first: " + array[0])
print("second: " + array[1])
print("third: " + array[2])

for element in array:
    print(element)

for index in range(10):
    print(index)

# Python tutorial:
# https://docs.python.org/3/tutorial/index.html
