# print(f'file_1 __name__: {__name__}')

# if __name__=="__main__":
#     print('"__something__" :- is called "Dunder"')

def add(x,y):
    return x+y

if __name__=="__main__":
    if add(1,2)==3:
        print("Pass")
    else:
        print("Fail")
        