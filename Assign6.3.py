#accpets number and count frequency of 2

#Buisiness Logic
def Count(No):
    iDigit=0
    iCnt = 0
    while(No>0):
        iDigit = No%10
        No = No // 10
        if(iDigit==2):
            iCnt = iCnt + 1
    
    return iCnt
        

#Main Function
def main():
    print("Please Enter the Number")
    Num = int(input())

    ret = Count(Num)
    print("Frequency of 2 is :",ret)


if __name__ == "__main__":
    main()

"""
Input - 252142
Output Frequency of 2 is : 3

"""