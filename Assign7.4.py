#Accept number and return its multiplication of digits

#Business Logic
def CountMult(No):
    Mult = 1
    iDigit = 0
    while(No!=0):
        iDigit = No % 10
        Mult = Mult * iDigit
        No = No // 10


    return Mult

#main Function
def main():
    print("Please Enter the number :")
    Num = int(input())

    Ret = CountMult(Num)
    print("Multiplication of Digits is :",Ret)


if __name__ == "__main__":
    main()

"""
Input - 335
Output - 45


"""