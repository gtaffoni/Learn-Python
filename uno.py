#!/user/bin/python

# This is just a test for github

"""
Created on Friday 24 Mar 2017
by giuliano.taffoni@inaf.it
"""


n = input("some integer value: ") # input from terminal

print n

n = "uno"

print(n)

'''
operands in python

    a + b
    a - b
    a * b
    a / b
    a**b
    a % b (modulo)
    or, and, not (logical operators)
    is, is not  (identity operators)
    is, in, not in (membership operators)

'''

z=1+1j #complex number

while abs(z)< 100:
    z = z**2 + 1
print z


a = [1,0,2,4]
for element in a:
    if element  == 0:
        continue
    print 1./element

message = 'hello there, how are you?'


for word in message.split():
    print (word)


