#to find the given number is prime or not

n = int(input("Enter any number: "))

if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")
else:
    print(number, "is not a prime number")