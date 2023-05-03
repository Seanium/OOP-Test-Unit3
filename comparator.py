import os
import shutil


def compare(fileNum):
    if os.path.exists("output1"):
        shutil.rmtree("output1")
    os.mkdir("output1")
    if os.path.exists("output2"):
        shutil.rmtree("output2")
    os.mkdir("output2")

    for i in range(fileNum):

        # run jar
        os.system(
            f"java -jar 1.jar < input/point{i}.txt > output1/result{i}.txt")
        os.system(
            f"java -jar 2.jar < input/point{i}.txt > output2/result{i}.txt")

        # open file
        with open(f"output1/result{i}.txt", 'r') as f1:
            list1 = f1.readlines()
        with open(f"output2/result{i}.txt", 'r') as f2:
            list2 = f2.readlines()

        # compare
        flag = 1
        for j in range(len(list1)):
            if list1[j] == list2[j]:
                pass
            else:
                flag = 0
                print(f"point {i} diff in line: {j+1}")
                break
        if flag == 1:
            print(f"right in point{i}")


if __name__ == '__main__':
    compare(fileNum=20)
