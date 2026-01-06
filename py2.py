# F-strings

# f_temp=67

# print(f'The tempeature is {(f_temp-32)/1.8:.2f} degrees Celcius')
# print(f'The tempeature is {(f_temp-32)/1.8:.2e} degrees Celcius')
# print(f'The tempeature is {(f_temp-32)/1.8:.2%} degrees Celcius')

# print(f'The tempeature is {(f_temp-32)/1.8:,.2f} degrees Celcius')

# f_temp_sun=27000000

# print(f'The temperature of the sun is {(f_temp_sun-32)/1.8:,.2f} degrees Celcius')
# print(f'The temperature of the sun is {(f_temp_sun-32)/1.8:15,.2f} degrees Celcius')
# print(f'The temperature of the sun is {(f_temp_sun-32)/1.8:<15,.2f} degrees Celcius')

# :[alignment][width],.[decimals][type]
# print(f'The temperature of the sun is {(f_temp_sun-32)/1.8:^15,.2f} degrees Celcius')


# Lists


# friends=["Paul","Dana", "Nathan","Lilly"]

# friends.append("Elina")
# friends.remove("Dana")
# # friends.sort()
# print(friends)
# print(len(friends))
# print(friends[2])

# [] :- List
# () :- Tuple 
# {} :- Set

#Dictonaries

contacts={
    'Bob':'ilvdog',
    'Wendy':'ilvcat',
    'Shibam':'ilvminors'
}

contacts['alex']='ilvnothing'
contacts.pop('Wendy')

for key in contacts.keys():
    if key =='Alex'.lower():
        print('Alex is in contacts')
        print(contacts)