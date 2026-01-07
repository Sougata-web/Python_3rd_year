# def add(a:float, b:float)->float:
#     return a+b

# print(add(11,10))
# print(add(11,12))
# print(add(11,13))

# def greet(name:str,greeting:str='Hi')->None:
#     print(f'{greeting}, {name}!')
    
# greet('Bob', 'Hello')
# greet('Sahil')

from matplotlib.pyplot import plot, show, title, xlabel, ylabel, axhline, legend

sunny_days=[11,25,23,52,5,46,24,7,4,34,24,6]
months=['jan','feb','mar','apr','may','jun','jul','aug','sept','oct','nov','dec']

avg_sunny_days=sum(sunny_days)/len(sunny_days)

plot(months,sunny_days,marker='o',color='red', label='Sunny Days')
title("Sunny Days by Months",fontsize=20)
xlabel("Months",fontsize=15)
ylabel("Sunny Days",fontsize=15)
axhline(avg_sunny_days, linestyle='--',color='cyan',label='Average')
legend()

show()