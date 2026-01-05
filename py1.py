# First class for python

# print("Hello World")

import time

def brew_tea():
    start_time=time.time()
    print("Brewing Tea...")
    time.sleep(1)
    print("Tea is ready.")
    end_time=time.time()
    print(f"Task time={end_time-start_time} seconds")
    
if __name__=="__main__":
    brew_tea()
    
    