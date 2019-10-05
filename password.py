import string
import random
username = input('please input your name:')
print(f"hi{username}, time to get a strong new password!")
user_choose = input('(C)omputer genarated or (M)anually typed? ')
if user_choose.lower() =='m':
    user_pass = input('please input password')
    if len(user_pass)<=3:
        print('weak password')
    if len(user_pass)>3 and len(user_pass)<=6:
        print('weak password')
    if len(user_pass)>6 and len(user_pass)<=8:
        print('strong password')
    if len(user_pass)>8:
        print('very strong password')
    if username in user_pass:
        print('do not use your name in your password as it can be easily guessed!')
else:
    def randomString(stringLength=10):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))


    print("Random password choice 1 is ", randomString())
    print("Random password choice 2 is ", randomString(10))
    print("Random password choice 3 is ", randomString(10))
