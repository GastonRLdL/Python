import sys

if (len(sys.argv) == 3):
    if sys.argv[1].isdigit() and sys.argv[2].isdigit():
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        print(f"sum:        {a + b}")
        print(f"Difference: {a - b}")
        print(f"Product:    {a * b}")
        if b == 0:
            print("Quotient:   ERROR (division by zero)")
            print("Reminder:   ERROR (modulo by zero)")
        else:
            print(f"Quotient:   {a / b}")
            print(f"Remainder:  {a % b}")    
    else:
        print("AssertionError: only intergers")
elif (len(sys.argv) > 3):
    print("AssertionError: too many arguments")