no=int(input("Enter number:"))
count=0
while(no>0):
    count=count+1
    no=no//10
print(f"the number of digits are: {count}")
