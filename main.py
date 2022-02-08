import random
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBER = '0123456789'
Symbol = "[]{}#()*;._-"

all = lower + upper + NUMBER + Symbol
length = 12
password = "".join(random.sample(all,length))
print("Your Generated Password is : ",password)