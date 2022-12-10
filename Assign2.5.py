#Accept Number from user and check weather number is even or odd

def CheckEven(No):
    if(No%2==0):
        print("Its Even Number")
    else:
        print("Its Odd Number")

#Main Function
def main():
    print("Please Enter the Number :")
    Num = int(input())

    CheckEven(Num)

if __name__ == "__main__":
    main()

    """
    Input - 12
    Output - Its Even Number
    Input - 7
    Output - Its Odd Number
    """