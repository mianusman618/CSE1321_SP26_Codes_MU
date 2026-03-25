states = ["Georgia", "Florida", "Alabama", "Tennessee", "S. Carolina"]
#numbers=[1,2,5,2,1,6,7]
print(states[5])
for index in range(len(states)):
    print(states[index])
    if "a" in states[index]:
        print("inside if statement")
        states[index]="ABC"
print(states)
