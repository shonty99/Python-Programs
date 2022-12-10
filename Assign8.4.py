#Accept N numbe from user and display all such elements which are divisible by 3 and divsible by 5

#Buisiness Logic
def Display(Brr,n):
    for i in range(0,n,1):
        if(Brr[i]%3==0)and(Brr[i]%5==0):
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