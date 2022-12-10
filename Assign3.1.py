#Accept Number from user print that number of even number on screen

#Business Logic
def Even(No):

    for i in range(1,(No*2)+1,1):
            if(i%2==0):
                print(i,end=" ")
                No = No-1

#Main Function
def main():
    print("Please Enter the Number:")
    Num = int(input())

    Even(Num)

if __name__ == "__main__":
    main()

"""
Input - 5
Output - 2 4 6 8 10

"""