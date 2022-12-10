#Accept Number from user and return difference between summation of all its factors and non factors

#Business Logic
def FactDiff(No):
    Fact = 0
    NonFact = 0
    for i in range(1,No,1):
        if(No%i==0):
            Fact = Fact + i
        else:
            NonFact = NonFact + i
    return(Fact-NonFact)


#Main Function
def main():
    print("Please Enter the Number:")
    Num = int(input())

    Result = FactDiff(Num)
    print("Difference between summation of Fact and Non Fact is ",Result)

if __name__ == "__main__":
    main()

    """
Input - 12
Output - -34

    """