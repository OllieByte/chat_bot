def greet(bot_name, birth_year):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")

def remind_name():
    print("Please, remind me your name.")
    your_name = input()
    # reading a name
    print(f"What a great name you have, {your_name}!")

def guess_age():
    print("Let me guess your age.\nEnter remainders of dividing your age by 3, 5, and 7.")
    remainder3 = int(input())
    remainder5 = int(input())
    remainder7 = int(input())
    your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    print(f"Your age is {your_age}; that's a good time to start programming!")

def counter():
    print("Now I will prove to you that I can count to any number you want.")
    user_int = int(input())
    count_up = 0
    while user_int >= count_up:
        print(count_up, "!")
        count_up += 1
    print("Completed, have a nice day!")

def test():
    print("Let's test your programming knowledge.")
    print("""Why do we use methods?
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.""")

    answer = int(input())

    while answer != 2:
        print("Please, try again.")
        answer = int(input())

    print("Congratulations, have a nice day!")



greet("Aid", 2025)
remind_name()
guess_age()
counter()
test()