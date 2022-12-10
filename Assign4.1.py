#Accept Number from user and display Multiplication of factors

#Business Logic
def FactMult(No):
    Ans=1
    for i in range(1,No,1):
        if(No%i==0):
            Ans = Ans * i
    return Ans


#Main Function
def main():
    print("Please Enter the number:")
    Num = int(input())

    Ret = FactMult(Num)

    print("Multiplication of factors are :",Ret)

if __name__ == "__main__":
    main()

    """
    Input - 12
    Output - 6 * 4 * 3 * 2 *1 = 144

    """