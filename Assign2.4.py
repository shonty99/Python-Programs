#Accepts two number from user and display first number in second number of times 

#Business Logic
def Display(No1,No2):
        for i in range(0,No2,1):
            print(No1,end=" ")

#Main Function
def main():
    print("Enter the First Number")
    Num1 = int(input())
    print("Enter the Second Number")
    Num2 = int(input())

    Display(Num1,Num2)

if __name__ == "__main__":
    main()

"""
Input - 12 5
Putput - 12 12 12 12 12
"""