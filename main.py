#WAP to check if a number is within the specified range
n=int(input("Enter an integer: "))
def in_range(n):
    #Range starts from -5 to +5; where -5 is in the range and +5 is outside
    if n in range(-5,5):
        print( str(n)+" is in the range")
        return True
    else :
        print("The number is outside the given range.")
        return False

print(in_range(n))