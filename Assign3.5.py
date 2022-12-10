#Accept Character and check it is vowel or not

#Business Logic
def ChkVowel(Value):
    
    if(Value.lower()=="a")or(Value.lower()=='e')or(Value.lower()=='i')or(Value.lower()=='o')or(Value.lower()=='u'):
        print("its Vowel")
    else:
        print("Not a Vowel")

#main Function
def main():
    print("Please enter Character :")
    Char = input()

    ChkVowel(Char)

if __name__ == "__main__":
    main()

"""
Input - A
Output - Its Vowel
Input - b
Output -  Not a Vowel
"""