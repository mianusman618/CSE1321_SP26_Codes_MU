if __name__=="__main__":
    global_counter=1
    count1=1
    while count1<=10:
        # print("Iter # ",count1)
        count1=count1+1
        count2=1
        while count2<=5:
            print(global_counter," I am here ")
            count2+=1
            global_counter+=1