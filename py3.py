# def add(a:float, b:float)->float:
#     return a+b

# print(add(11,10))
# print(add(11,12))
# print(add(11,13))

def greet(name:str,greeting:str='Hi')->None:
    print(f'{greeting}, {name}!')
    
greet('Bob', 'Hello')
greet('Sahil')