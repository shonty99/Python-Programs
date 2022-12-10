#Accept a number from user and print even factors of that number

#Business Logic
def EvenFactor(No):
    for i in range(1,No,1):
        if(No%i==0)and(i%2==0):
            print(i,end=" ")

#Main Function
def main():
    print("Enter the number :")
    Num = int(input())

    EvenFactor(Num)

if __name__  == "__main__":
    main()

"""
Input - 12
Output - 2 4 6
"""