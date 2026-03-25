states = ["Georgia", "Florida", "Alabama", "Tennessee", "S. Carolina"]
#numbers=[1,2,5,2,1,6,7]
for i in range(len(states)):
    print(states[i])
    if "a" in states[i]:
        states[i]="ABC"
print(states)
