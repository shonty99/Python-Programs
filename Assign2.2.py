#Accept number and print that number of * using while loop

#Business Logic
def Display(No):
    while(No>0):
        print("*",end=" ")
        No = No-1


#main Function
def main():
    print("Enter the Number:")
    Num = int(input())

    Display(Num)

if __name__ == "__main__":
    main()

"""
Input - 5
Output - * * * * *
"""