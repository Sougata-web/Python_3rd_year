# from typing import Generator

# data:range=range(10000)

# squared:Generator[int,None,None]=(pow(n,2) for n in data)

# # print(squared)
# print(next(squared))
# print(next(squared))
# print(next(squared))
# print(next(squared))
# print(next(squared))
# print(next(squared))
# print(next(squared))

# data:list[tuple[str,int]]=[('a',1),('b',2),('c',3)]
# my_dict:dict[str,int]={hash(k):v*10 for k, v in data}
# print(my_dict)

# unicode_string=u'aabbA'
# ascii_string=unicode_string.encode('ascii','ignore')
# print(ascii_string)

squares={
    1:1,
    2:4,
    3:9
}

for key in squares:
    print(key, end=' ')

print()
for values in squares.values():
    print(values, end=' ')
print()
    
for k,v in squares.items():
    print(f'Key:{k} Value:{v},',end=' ')