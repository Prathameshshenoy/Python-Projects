#A palindrome is a number that is the same when it is reversed, for example 2123212 is a palindrome, write a program to check if a number is a palindrome.

num = int(input("Enter number:"))
a = num
pal = 0
while(num>0):
    digit = num % 10
    pal = pal * 10 + digit
    num = num//10
if (a==pal):
    print("The number is a palindrome")
else:
    print("The number isn't a palindrome")
