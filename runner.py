import generator
import comparator

fileNum = 10
instrNum = 10000
iterateNum = 5


def run_iterate(iterateNum=iterateNum):
    for i in range(iterateNum):
        print(f"iteration {i}")
        generator.makeInputs(fileNum=fileNum, instrNum=instrNum)
        comparator.compare(fileNum=fileNum)


def run_single():
    generator.makeInputs(fileNum=fileNum, instrNum=instrNum)
    comparator.compare(fileNum=fileNum)


run_single()
# run_iterate()
