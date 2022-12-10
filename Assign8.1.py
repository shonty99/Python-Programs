#Accpet N number from user and return diff between summation of even elements and summation of odd elements

#Business Logic
def Diff(Brr,n):
    EvenSum = 0
    OddSum = 0
    Diff = 0 
    #print(Brr[1])
    for i in range(0,n,1):
        if(Brr[i]%2==0):
            EvenSum = Brr[i] + EvenSum
        else:
            OddSum = OddSum + Brr[i]

    Diff =  EvenSum - OddSum

    return Diff

#Main Function
def main():
    Arr = []
    print("Enter the Size :")
    N = int(input())
    print("Please enter the elements :")
    for i in range(0,N):
        ele = int(input())
        Arr.append(ele)
    
    print(Arr)

    Ret = Diff(Arr,N)

    print("The Difference between sum of Even and Odd is :",Ret)

if __name__ == "__main__":
    main()

"""
Input -
        N        : 6
        Elements : 85 66 3 80 93 88
Output -
        53 (234 - 181)


"""