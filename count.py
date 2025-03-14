fname = input('Enter the name of your text: ' )
doc = open(fname)
dic =dict()

for line in doc:
    word = line.rstrip()
    n_word = line.split()
    print(n_word)
    for wrd in n_word:
        dic[wrd]= dic.get(wrd, 0) +1
print(dic)

lis = []

for k,v in dic.items():
    tup = (v,k)
    lis.append(tup)
print(lis)
new = sorted(lis, reverse=True) 
for k,v in new[:10]:
    print(k,v)


for line in doc:
    line = line.rstrip()
    if line.find('From')>= 0:
        print(line)

import re
for line in doc:
    line = line.rstrip()
    if re.search('^From', line):
        print(line)


x = 'My 2 favourite numbers are 12 and 45'
y = re.findall('[0-9]+', x)
print(y)

import socket
my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect(('data.pr4e.org', 80))