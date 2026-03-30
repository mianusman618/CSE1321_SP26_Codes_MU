r1=int(input("Enter Rows for Mat A"))
c1=int(input("Enter Columns for Mat A"))
r2=int(input("Enter Rows for Mat B"))
c2=int(input("Enter Columns for Mat B"))
if c1!=r2:
    print("Multiplication not possible")
elif c1==r2:
    values_A=input("Enter comma seprated values for A ")
    values_B = input("Enter comma seprated values for B ")
    #1,2,3,4
    values_A_list=values_A.split(",")
    values_B_list=values_B.split(",")
    #print(values_A_list)
    for i in range(len(values_A_list)):
        values_A_list[i]=int(values_A_list[i])
    #print(values_A_list)
    mat_A=[]
    index=0
    for i in range(r1):
        row=[]
        for c in range(c1):
            row.append(values_A_list[index])
            index+=1
        #print(row)
        mat_A.append(row)
    #print(mat_A)
    ###########Matrix B#######
    for i in range(len(values_B_list)):
        values_B_list[i]=int(values_B_list[i])
    #print(values_B_list)
    mat_B=[]
    index=0
    for i in range(r2):
        row=[]
        for c in range(c2):
            row.append(values_B_list[index])
            index+=1
        #print(row)
        mat_B.append(row)
    #print(mat_B)
    print("Matrix A")
    for i in range(r1):
        for c in range(c1):
            print(mat_A[i][c],end=" ")
        print()
    print("Matrix B")
    for i in range(r1):
        for c in range(c1):
            print(mat_B[i][c], end=" ")
        print()

    result_mat=[]
    for r in range(r1):
        row=[]
        for c in range(c2):
            row.append(0)
        result_mat.append(row)
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result_mat[i][j]+=mat_A[i][k]*mat_B[k][j]
    print("Result Matrix ")
    for i in range(r1):
        for c in range(c2):
            print(result_mat[i][c], end=" ")
        print()