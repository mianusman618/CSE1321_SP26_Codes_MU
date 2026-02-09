from itertools import count

if __name__=="__main__":
    total_iter=0

    for i in range(5):
        print("Outer loop Iteration # ", i)
        count=0
        while count<3:
            print("Inner loop Iteration # ",count)
            count+=1
            total_iter+=1

    print("Total Iteration ",total_iter)