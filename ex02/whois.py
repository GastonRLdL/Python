import sys

if len(sys.argv) == 2:
    
    num = (sys.argv[1::])
    if num[0].isdigit() == True:
        n = int(num[0])
        if n == 0:
            print("I'm 0")
        elif n % 2 == 0:
            print("I'm Even")
        else:
            print("I'm Odd")
else:
    exit