#Accept a number from user and count no of odd digits

#Business Logic
def CountOdd(No):
    iCnt = 0
    iDigit = 0
    while(No!=0):
        iDigit = No % 10
        No = No // 10

        if(iDigit%2!=0):
            iCnt = iCnt + 1

    return iCnt

#main Function
def main():
    print("Please Enter the number :")
    Num = int(input())

    Ret = CountOdd(Num)
    print("Number of Odd Digits are :",Ret)


if __name__ == "__main__":
    main()

"""
Input - 2395
Output -3


"""