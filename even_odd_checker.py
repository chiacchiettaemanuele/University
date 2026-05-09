def even_odd_checker(num):
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")

def main():
    number = int(input("type the number: "))
    even_odd_checker(number)

main()
