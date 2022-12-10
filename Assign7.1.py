#Accept number from user and return the count of even numbers

#Business Logic
def CountEven(No):
    iDigit = 0
    iCnt = 0 
    while(No!=0):
        iDigit = No % 10
        No = No // 10
        if(iDigit%2==0):
            iCnt = iCnt + 1
    
    return iCnt


#Main Function
def main():
    print("Please enter the number :")
    Num = int(input())

    Ret = CountEven(Num)
    print("The number of Even digits are :",Ret)

if __name__ == "__main__":
    main()

"""
Input - 8452
Output - The number of Even digits are : 3
"""