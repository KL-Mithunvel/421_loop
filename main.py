from num_op import *

num = int(input("Enter any number: "))
num_path = [num, ]
i=0
while True:
    next_num = calc(num)
    num_path.append(next_num)
    print(num_path[-1])
    if next_num == 4:
        num_path.append(2)
        num_path.append(1)
        print(num_path[-2])
        print(num_path[-1])
        print("length: ", len(num_path))
        print("421 loop achieved")
        print(num_path)
        break
    num = next_num
    i = i+1
