#Program to find number is divisible by 5 or not
#Business Logic
def Divisible(No):
    if(No%5==0):
        return True
    else:
        return False

#Main Function
def main():
    print("Please Enter the Number")
    Num = int(input())

    Return = Divisible(Num)

    if(Return == True):
        print("Given no is Divisible by 5")
    else:
        print("Given no is not Divisible by 5")


if __name__ == "__main__":
    main()

"""
Input - 50
Output - Given No is divisible by 5
"""