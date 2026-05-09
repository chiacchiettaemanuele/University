def prime_number(n):
    for i in range(2, n):
        if n % i == 0:
           return 0
    return 1

def main():
     number=int(input("digita il numero"))
     if prime_number(number)==1:
        print("primo")
     else:
        print("non primo")
main()