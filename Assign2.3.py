#Accept number from user of number is less than 10 print hello otherwise print demo

#Business Logic
def Condition(No):
    if(No<10):
        print("Hello")
    else:
        print("Demo")

#Main Function
def main():
    print("Please Enter the Number :")
    Num = int(input())

    Condition(Num)

if __name__ == "__main__":
    main()

"""
input - 5
Output - Hello
input - 12
Output - Demo
"""