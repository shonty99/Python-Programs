#Accept Number from user and return difference between summation between even and odd digits

#Business Logic
def CountDiff(No):
    SumEven = 0
    SumOdd = 0
    iDigit = 0
    while(No!=0):
        iDigit = No % 10
        No = No // 10
        if(iDigit%2==0):
            SumEven = SumEven + iDigit
        else:
            SumOdd = SumOdd + iDigit

        Diff = SumEven - SumOdd

    return  Diff

#main Function
def main():
    print("Please Enter the number :")
    Num = int(input())

    Ret = CountDiff(Num)
    print("Difference  is :",Ret)


if __name__ == "__main__":
    main()

"""
Input : 2395
Output : -15(2-7)


"""