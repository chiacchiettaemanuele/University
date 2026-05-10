import random

def random_number():
    return random.randint(1, 6)



def main():
    input("Press enter to roll the dice!!!")
    numbers = random_number()
    print(numbers)
    if numbers==6:
      print("winner!!")
    else:
        print("Try again!!")

main()

