i = 0
max = 0
x = 0
count = 0
avg = 0
min = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000
while i ==0:
    num = int(input('num: '))
    count = count +1
    x = x+ num
    if num > max:
        max = num
    if num < min and num >=0:
        min = num
    if num == -1:
        break
    avg = x/count
print(f"maximum number = {max}, minimum number = {min} , avg of the numbers = {avg}")
