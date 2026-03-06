print("Please enter the column letter and row number to figure out where you are in the Marietta Campus")
col=input("Enter Column = ")
row=int(input("Enter row ="))
if col=="N":
    if row==11 or row==10 or row==9:
        print("Atrium Building")