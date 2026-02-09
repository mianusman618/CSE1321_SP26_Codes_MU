if __name__=="__main__":
    user_num=int(input("Enter a number to see its table : "))
    print(f"Multiplication table of {user_num}")
    for i in range(1,11):
        print(f"{user_num} * {i} = {user_num*i}")