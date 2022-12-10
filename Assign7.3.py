#Accept a number and return count of digits in between 3 and 7

#Business Logic
def Count(No):
    iCnt = 0
    iDigit = 0
    while(No!=0):
        iDigit = No % 10
        
        if(3<iDigit<7):
            iCnt = iCnt + 1
        No = No // 10

    return iCnt

#main Function
def main():
    print("Please Enter the number :")
    Num = int(input())

    Ret = Count(Num)
    print("Number of  Digits between 3 and 7 are :",Ret)


if __name__ == "__main__":
    main()

"""
Input - 3355
Output -2


"""