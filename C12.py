if __name__=="__main__":
    secret_num=4
    user_input=int(input("Enter a number between 1-10 : "))
    while True:
        if user_input < 1 or user_input > 10:
            user_input=int(input("Wrong input Please enter a number between 1-10 : "))
        elif user_input==secret_num:
            print("Congrats you guessed it right")
            break
        elif user_input>secret_num:
            print("Guess is higher")
            user_input = int(input("Please enter a number between 1-10 : "))
        elif user_input<secret_num:
            print("Guess is Lower than sec num")
            user_input = int(input("Please enter a number between 1-10 : "))