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

# contacts={
#     'Bob':'ilvdog',
#     'Wendy':'ilvcat',
#     'Shibam':'ilvminors'
# }

# contacts['alex']='ilvnothing'
# contacts.pop('Wendy')

# for key in contacts.keys():
#     if key =='Alex'.lower():
#         print('Alex is in contacts')
#         print(contacts)


# Error handling

# try:
#     numerator=float(input("Enter numerator: "))
#     denominator=float(input("Enter denominator: "))
#     quotient=numerator/denominator
#     print(f'The qoutient is {quotient}')
    
# # except:
# #     print('Invalid Inputs')

# except ValueError:
#     print('Invalid inputs. Please enter a number.')
# except ZeroDivisionError:
#     print('Invalid Input. Please enter a non-zero denominator.')

# List comprehensions 
# [(operation) (for var in) (org_list)]

nums=[1,2,3,4,5]

# nums_squared=[]
# for n in nums:
#     square=n**2
#     nums_squared.append(square)
    
# print(nums_squared)

# nums_squared=[n**2 for n in nums]
# print(nums_squared)

# tv_shows=['friends', 'PARKS AND RECREATION', 'the office', '30 rock', 'modern FAMILY']

# tv_shows_cap=[]

# for show in tv_shows:
#     show_cap=show.title()
#     tv_shows_cap.append(show_cap)
    
# print(tv_shows_cap)

# tv_shows_cap=[show.title() for show in tv_shows]
# print(tv_shows_cap)

# tv_show_cap=[show.title() for show in tv_shows if len(show) >= 10]
# print(tv_show_cap)