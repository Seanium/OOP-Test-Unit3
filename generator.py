import random
import string
import os
import shutil

INT_MAX = 2**31-1
INT_MIN = -2**31

ID_MIN = 0
ID_MAX = 9999

P_ADD = 0.1
P_EXIST = 0.9

people = set()
groups = set()
messages = set()  # 在send后，有意不删除消息


def ran_int(min=INT_MIN, max=INT_MAX):
    return random.randint(min, max)


def ran_str(min=1, max=10):
    return ''.join(random.sample(string.ascii_letters + string.digits + string.punctuation, ran_int(min, max)))

# 概率p生成已存在id，概率1-p生成任意id


def ran_id(set, p):
    ran_p = random.random()
    # 生成任意id
    if(ran_p > p or len(set) == 0):
        id = ran_int(ID_MIN, ID_MAX)
        set.add(id)
    # 生成已存在id
    else:
        id = set.pop()
        set.add(id)
    return id


def ran_pid(p):
    return ran_id(people, p)


def ran_gid(p):
    return ran_id(groups, p)


def ran_mid(p):
    return ran_id(messages, p)


def add_person(p=P_ADD):
    instr = "ap {id} {name} {age}".format(
        id=ran_pid(p), name=ran_str(), age=ran_int(0, 200))
    return instr


def add_relation(p=P_EXIST):
    instr = "ar {id1} {id2} {value}".format(
        id1=ran_pid(p), id2=ran_pid(p), value=ran_int(1, 100))
    return instr


def query_value(p=P_EXIST):
    instr = "qv {id1} {id2}".format(id1=ran_pid(p), id2=ran_pid(p))
    return instr


def query_circle(p=P_EXIST):
    instr = "qci {id1} {id2}".format(id1=ran_pid(p), id2=ran_pid(p))
    return instr


def query_block_sum():
    instr = "qbs"
    return instr


def query_triple_sum():
    instr = "qts"
    return instr


def add_group(p=P_ADD):
    instr = "ag {gid}".format(gid=ran_gid(p))
    return instr


def add_to_group(p=P_EXIST):
    instr = "atg {pid} {gid}".format(pid=ran_pid(p), gid=ran_gid(p))
    return instr


def del_from_group(p=P_EXIST):
    instr = "dfg {pid} {gid}".format(pid=ran_pid(p), gid=ran_gid(p))
    return instr


def query_group_value_sum(p=P_EXIST):
    instr = "qgvs {gid}".format(gid=ran_gid(p))
    return instr


def query_group_age_var(p=P_EXIST):
    instr = "qgav {gid}".format(gid=ran_gid(p))
    return instr


def modify_relation(p=P_EXIST):
    instr = "mr {id1} {id2} {value}".format(
        id1=ran_pid(p), id2=ran_pid(p), value=ran_int(-100, 100))
    return instr


def query_best_acquaintance(p=P_EXIST):
    instr = "qba {id}".format(id=ran_pid(p))
    return instr


def query_couple_sum():
    instr = "qcs"
    return instr


def add_message(p=P_ADD):
    type = ran_int(0, 1)
    toId = ran_pid(P_EXIST) if type == 0 else ran_gid(P_EXIST)
    instr = "am {mid} {socialValue} {type} {fromId} {toId}".format(
        mid=ran_mid(p), socialValue=ran_int(-1000, 1000),
        type=type, fromId=ran_pid(P_EXIST), toId=toId)
    return instr


def send_message(p=P_EXIST):
    instr = "sm {id}".format(id=ran_mid(p))
    return instr


def query_social_value(p=P_EXIST):
    instr = "qsv {id}".format(id=ran_pid(p))
    return instr


def query_received_messages(p=P_EXIST):
    instr = "qrm {id}".format(id=ran_pid(p))
    return instr


instrs = [add_person, add_relation, query_value, query_circle, query_block_sum,
          query_triple_sum, add_group, add_to_group, del_from_group, query_group_value_sum,
          query_group_age_var, modify_relation, query_best_acquaintance, query_couple_sum, add_message,
          send_message, query_social_value, query_received_messages]
more_qts = [query_triple_sum] * 5
instrs += more_qts


def makeInstrs(instrNum, fileName):
    with open(fileName, 'w') as f:
        for i in range(instrNum):
            print(instrs[ran_int(0, len(instrs) - 1)](), file=f)


def makeInputs(fileNum, instrNum):
    if os.path.exists("input"):
        shutil.rmtree("input")
    os.mkdir("input")
    for i in range(fileNum):
        fileName = f"input/point{i}.txt"
        makeInstrs(instrNum, fileName)


if __name__ == '__main__':
    makeInputs(fileNum=20, instrNum=10000)
