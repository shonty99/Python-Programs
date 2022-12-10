#Accept one number from user and convert its case

#Business Logic
def Convert(Value):
    print(Value.swapcase())

#Main Function
def main():
    print("Enter Character:")
    Char = input()

    Convert(Char)

if __name__ == "__main__":
    main()

"""
Input - A
Output - a
"""