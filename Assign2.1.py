#Program to take input number from user and print that number of *

#Business Logic
def Display(No):
    for i in range(0,No,1):
        print("*",end=" ")

#Main Function
def main():
    print("Please Enter the number:")
    Num = int(input())

    Display(Num)


if __name__ == "__main__":
    main()

"""
Input - 5
Output - * * * * *
"""