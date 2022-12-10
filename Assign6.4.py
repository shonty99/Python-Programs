#Accpets number from user and count the frequency of 4 

#Business Logic
def Count(No):
    iCnt = 0
    iDigit = 0
    while(No>0):
        iDigit = No % 10
        No = No // 10
        if(iDigit==4):
            iCnt = iCnt + 1
    
    return iCnt

#Main Function
def main():
    print("Please enter the Number :")
    Num = int(input())

    Ret = Count(Num)
    print("Frequency of 4 is :",Ret)

if __name__ == "__main__":
    main()

"""
Input - 4452
Output - Frequency of 4 is : 2

"""