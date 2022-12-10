#Accpets number from user and count frequency of such a digits which are less than 6 

#Business Logic
def Count(No):
    iCnt = 0
    iDigit = 0
    
    while(No>0):
        iDigit = No % 10
        No = No // 10
        if(iDigit<6):
            iCnt = iCnt + 1
    
    return iCnt

#Main Function
def main():
    print("Please enter the Number :")
    Num = int(input())

    Ret = Count(Num)
    print("Frequency of digits less than 6 :",Ret)

if __name__ == "__main__":
    main()

"""
Input - 12599
Output - Frequency of digits less than 6 : 3

"""