#Accept N numbe from user and display all such elements which are multiples of 11

#Buisiness Logic
def Display(Brr,n):
    for i in range(0,n,1):
        if(Brr[i]%11==0):
            print(Brr[i])
            
#Main Function
def main():
    Arr = []
    print("Enter the size :")
    N = int(input())

    print("Please enter the elements")
    for i in range(0,N,1):
        ele = int(input())
        Arr.append(ele)

    Display(Arr,N)


if __name__ == "__main__":
    main()