#Accept Number from user and return alll its summation of non factors

#Business Logic
def SumNonFact(No):
    Add = 0
    for i in range(1,No,1):
        if(No%i!=0):
            Add = Add  + i
    return Add



#Main Function
def main():
    print("Please Enter the Number :")
    Num = int(input())

    Result = SumNonFact(Num)
    print("Summation of Non Factors is :",Result)

if __name__ == "__main__":
    main()