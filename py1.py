# First class for python

# print("Hello World")

import time

#How to use decorators

# def brew_tea():
#     start_time=time.time()
#     print("Brewing Tea...")
#     time.sleep(1)
#     print("Tea is ready.")
#     end_time=time.time()
#     print(f"Task time={end_time-start_time} seconds")
    
# if __name__=="__main__":
#     brew_tea()
    
# def timer_dec(base_fn):
#     def enhanced_fn():
#         start_time=time.time()
#         base_fn()
#         end_time=time.time()
#         print(f"Task time={end_time-start_time} seconds")
#     return enhanced_fn

# def brew_tea():
#     print("Brewing Tea...")
#     time.sleep(1)
#     print("Tea is ready.")
    
    
# dec_brew_tea=timer_dec(brew_tea)
# dec_brew_tea()
        
# def timer_dec(base_fn):
#     def enhanced_fn():
#         start_time=time.time()
#         base_fn()
#         end_time=time.time()
#         print(f"Task time={end_time-start_time} seconds")
#     return enhanced_fn

# def brew_tea():
#     print("Brewing Tea...")
#     time.sleep(1)
#     print("Tea is ready.")
    
    
# brew_tea=timer_dec(brew_tea)
# brew_tea()


# def timer_dec(base_fn):
#     def enhanced_fn():
#         start_time=time.time()
#         base_fn()
#         end_time=time.time()
#         print(f"Task time={end_time-start_time} seconds")
#     return enhanced_fn

# @timer_dec
# def brew_tea():
#     print("Brewing Tea...")
#     time.sleep(1)
#     print("Tea is ready.")
  
# brew_tea()


def timer_dec(base_fn):
    def enhanced_fn(*args):
        start_time=time.time()
        base_fn(*args)
        end_time=time.time()
        print(f"Task time={end_time-start_time} seconds \n")
    return enhanced_fn

@timer_dec
def brew_tea():
    print("Brewing Tea...")
    time.sleep(1)
    print("Tea is ready.")
 
@timer_dec
def make_matcha(tea_type,steep_time):
    print(f'Making {tea_type} matcha tea...')
    time.sleep(steep_time)
    print("Matcha is ready")
    
make_matcha("Green",1)
brew_tea()