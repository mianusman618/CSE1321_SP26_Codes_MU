if __name__=="__main__":
    secret_num=4
    user_input=int(input("Enter a number between 1-10 : "))
    while user_input < 1 or user_input > 10:
        user_input=int(input("Wrong input Please enter a number between 1-10 : "))
    if user_input==secret_num:
        print("Congrats you guessed it right")
    else:
        print("Wrong Guess Try again")