# def add(a:float, b:float)->float:
#     return a+b

# print(add(11,10))
# print(add(11,12))
# print(add(11,13))

# def greet(name:str,greeting:str='Hi')->None:
#     print(f'{greeting}, {name}!')
    
# greet('Bob', 'Hello')
# greet('Sahil')

# from matplotlib.pyplot import plot, show, title, xlabel, ylabel, axhline, legend

# sunny_days=[11,25,23,52,5,46,24,7,4,34,24,6]
# months=['jan','feb','mar','apr','may','jun','jul','aug','sept','oct','nov','dec']

# avg_sunny_days=sum(sunny_days)/len(sunny_days)

# plot(months,sunny_days,marker='o',color='red', label='Sunny Days')
# title("Sunny Days by Months",fontsize=20)
# xlabel("Months",fontsize=15)
# ylabel("Sunny Days",fontsize=15)
# axhline(avg_sunny_days, linestyle='--',color='cyan',label='Average')
# legend()

# show()

# import matplotlib.pyplot as plt

# sunny_days=[11,25,23,52,5,46,24,7,4,34,24,6]
# months=['jan','feb','mar','apr','may','jun','jul','aug','sept','oct','nov','dec']

# avg_sunny_days=sum(sunny_days)/len(sunny_days)

# plt.plot(months,sunny_days,marker='o',color='red', label='Sunny Days')
# plt.title("Sunny Days by Months",fontsize=20)
# plt.xlabel("Months",fontsize=15)
# plt.ylabel("Sunny Days",fontsize=15)
# plt.axhline(avg_sunny_days, linestyle='--',color='cyan',label='Average')
# plt.legend()

# plt.show()

# import time
# from tqdm import tqdm

# for i in tqdm(range(0,50),desc='Processing',bar_format='{desc}: |{bar}| {percentage:.1f}%'):
#     time.sleep(0.1)

# import time
# from tqdm import tqdm

# for i in tqdm(range(0,50)):
#     time.sleep(0.1)


# import time
# from tqdm import tqdm

# bar_format=(
#     '{desc}: |{bar}| {percentage:.1f}%'
#     '[ {n_fmt}/{total_fmt} iterations, '
#     'Elapsed: {elapsed}, '
#     'Remaining: {remaining}, '
#     'Rate: {rate_fmt}]'
# )

# for i in tqdm(range(0,50),desc='Processing',bar_format=bar_format,colour='magenta'):
#     time.sleep(0.1)

# x:int=10
# weather:str='Cloudy'
# print(weather)

# weather='sunny'
# print(weather)
# data:dict[str,int]={'bob':1,'sahil':2}
# print(data)

# def get_data()->dict[str,int]:
#     return {'a':1,'b':2}

# def greet_people(people:list[str])->None:
#     for person in people:
#         print(f'Hello, {person.capitalize()}!')
        
# greet_people(['Bob','James'])

from joblib import Parallel,delayed
import time

my_list:list[int]=[1,2,3,4]
my_squares:list[int]=[]
start=time.time()
def slow_square(i)->int:
    squared:int=i*i
    return squared

parallel_obj=Parallel(n_jobs=-1)

my_squares=parallel_obj(delayed(slow_square)(i) for i in my_list)

print(my_squares)
end=time.time()
print(f'Time used: {end-start}sec')