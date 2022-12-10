#Write a program which accept a number and check weather it contains 0 or not

#Business Logic
def ChkZero(No):
    while(No>1):
        iDigit = No % 10
        No = No//10 
        if(iDigit==0):
            return True
        else:
            return False


#Main Function
def main():
    print("Please Enter a number:")
    Num = int(input())

    Return = ChkZero(Num)
    if(Return == True):
        print("It contains Zero")
    else:
        print("There is no zero")


if __name__ == "__main__":
    main()

"""
Input - 1204
Output - It contains Zero
"""