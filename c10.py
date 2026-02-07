if __name__=="__main__":
    u_input = input("Enter a grade or (999 to quit) : ")
    u_input=int(u_input)
    while u_input != 999:
        print("Inside loop")
        u_input = input("Enter a grade or 999 to quit : ")
        u_input = int(u_input)
    print("Outside loop")