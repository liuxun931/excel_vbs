from scapy.all import * 
import os
from decimal import Decimal

file1_name = "/home/admin/Downloads/packet-scbond1.pcap"
file2_name = "/home/admin/Downloads/packet-scbond2.pcap"

#file1 = PcapReader(file1_name)
#file2 = PcapReader(file2_name)

def read_files():
    file1 = PcapReader(file1_name)
    file2 = PcapReader(file2_name)
    return file1,file2

file1, file2 = read_files()

print("read file finished.")


### save data to files ###
'''
os.system("touch ./dict1.txt")
os.system("touch ./dict2.txt")

def save_data_to_file(pcap, filename):
    for i in pcap:
        row = str(i.seq) + '_' + str(i.ack) + ' ' + str(i.time)
        os.system("echo %s >> %s" %(row, filename))

save_data_to_file(file1, 'dict1.txt')
save_data_to_file(file2, 'dict2.txt')

'''
###  end save data to file ###



### create new dict for calculate ###
list_idx1 = os.popen("cat ./dict1.txt|awk '{print $1}'").read().split('\n')
list_key1 = os.popen("cat ./dict1.txt|awk '{print $2}'").read().split('\n')
list_idx1.pop()
list_key1.pop()
dict1 = dict(zip(list_idx1, list_key1))

list_idx2 = os.popen("cat ./dict2.txt|awk '{print $1}'").read().split('\n')
list_key2 = os.popen("cat ./dict2.txt|awk '{print $2}'").read().split('\n')
list_idx2.pop()
list_key2.pop()
dict2 = dict(zip(list_idx2, list_key2))

pub_idx = set(dict1.keys()).intersection(set(dict2.keys()))
print("finished load dicts...")
print("show time gap: ")
os.system('echo "" > time_gap.txt')
for i in pub_idx:
    time_gap = Decimal(dict1[i]) - Decimal(dict2[i])
    os.system("echo %s >> time_gap.txt" %time_gap)
    print(time_gap)





### read data from files ###

'''

list1 = os.popen('cat ./dict1.txt').read().split('\n')
list1.pop()
list2 = os.popen('cat ./dict2.txt').read().split('\n')
list2.pop()

for i in list1:
    id1 = i.split(' ')[0]
    time1 = i.split(' ')[1]
    for j in list2:
        id2 = j.split(' ')[0]
        time2 = j.split(' ')[1]
        if id1 == id2:
            print("found packet: ")
            print(id1)
            time_gap = float(time2) - float(time1) 
            print("time_gap = %d" %time_gap)
'''


'''
def get_dict(afile):
    for i in afile:
        adict = {}
        items = str(i.seq) + '_' + str(i.ack)
        keys = i.time
        adict[items] = keys
    return adict

dict1 = get_dict(file1)
dict2 = get_dict(file2)

print("finished collect data to dict.")

check_list = dict1.items() & dict2.items()

print(check_list)

print("start calculating time")
for i in check_list:
    gap = dict2[i] - dict1[i]
    print("seq_ack = %s, time gap = %d" %(i, gap)) 

print("all finished.")

'''

'''
list1 = []
list2 = []

def seq_list(afile, alist):
    for i in afile:
        alist.append(i.seq)
    return alist

list1 = seq_list(file1, list1)
list2 = seq_list(file2, list2)

list3 = set(list1).intersection(set(list2))
print("length: list1 = %s, list2 = %s, list3 = %s" %(len(list1), len(list2), len(list3)))

'''


#file1, file2 = read_files()

### get data [seq_ack : time] into 2 dict. then compare dict.## 

