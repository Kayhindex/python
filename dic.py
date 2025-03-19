d = {}

d['name']= 'Kenny'
d['name1'] = 'Taiwo'
d['name2'] = 'Emma'
# print(d)

d.setdefault('name3')
print(d)
print(d['name2'])
print(d.get('name2', 0) *3)
# print(d['name1'])

# for k in d.values():
#     print(k)
k ={}
b = k.fromkeys(['a', 'b', 'c'])
print(b)

print(d)