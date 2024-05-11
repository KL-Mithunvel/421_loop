from num_op import *
from achivedLoop import *
num = int(input("Enter any number: "))
num_path = [num, ]
while True:
    next_num = calc(num)
    num_path.append(next_num)
    print(num_path[-1])
    if next_num == 4:
        enterLoop(num_path)
        print("421 loop achieved")
        break

    elif next_num == -1:
        enterLoop(num_path)
        print("N1 loop achieved")
        break

    elif next_num == -5:
        enterLoop(num_path)
        print("N5 loop achieved")
        break

    elif next_num == -17:
        enterLoop(num_path)
        print("N17 loop achieved")
        break

    num = next_num

print(num_path)
print("length: ", len(num_path))


