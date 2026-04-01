r1=int(input("Enter the rows for Mat A = "))
c1=int(input("Enter the Cols for Mat A = "))

r2=int(input("Enter the rows for Mat B = "))
c2=int(input("Enter the Cols for Mat B = "))

if c1!=r2:
    print("Matrix multiplication is not possible.")
elif c1==r2:
    values_A=input("Enter Values for A comma seprated = ")
    values_B = input("Enter Values for B comma seprated = ")
    # print(values_A)
    values_A_list=values_A.split(",")
    values_B_list = values_B.split(",")
    # print(values_A_list)
    for i in range(len(values_A_list)):
        values_A_list[i]=int(values_A_list[i])
    for i in range(len(values_B_list)):
        values_B_list[i]=int(values_B_list[i])
    #print(values_A_list)
    # print(values_B_list)
    mat_A=[]
    index=0
    for i in range(r1):
        row=[]
        for k in range(c1):
            row.append(values_A_list[index])
            index+=1
        mat_A.append(row)
    #print(mat_A)
    ########################################
    mat_B = []
    index = 0
    for i in range(r2):
        row = []
        for k in range(c2):
            row.append(values_B_list[index])
            index += 1
        mat_B.append(row)
    #print(mat_B)
    print("Matrix A")
    for i in range(r1):
        for c in range(c1):
            print(mat_A[i][c],end=" ")
        print()
    print("Matrix B")
    for i in range(r2):
        for c in range(c2):
            print(mat_B[i][c], end=" ")
        print()

    result = []
    index = 0
    for i in range(r1):
        row = []
        for k in range(c2):
            row.append(0)
            index += 1
        result.append(row)


    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j]+=mat_A[i][k]*mat_B[k][j]



    print("Result ")
    for i in range(r1):
        for c in range(c2):
            print(result[i][c], end=" ")
        print()