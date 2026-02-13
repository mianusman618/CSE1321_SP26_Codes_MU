if __name__ == "__main__":
    choice = int(input("Enter a number to see the table: "))
    for var in range(4):
        print("Table of ", choice)
        for multiplier in range(1,11):
            print(str(multiplier) + " * " + str(choice) + " = " + str(multiplier * choice))
