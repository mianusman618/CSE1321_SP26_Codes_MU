if __name__=="__main__":
    Far=input("Enter Far Temp : ")
    Far=float(Far)
    kelvin=(Far-32)*5/9+273.15
    #print("Your weight on the moon is = ",moon_weight,"lb")
    print(f"Your weight on the moon is = {kelvin:.2f} lb")