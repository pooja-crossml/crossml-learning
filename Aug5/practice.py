import pdb

cars = ['Hundai', 'Maruti', 'Scorpio', 'Tesla']
# pdb.set_trace()
# breakpoint() #same as pdb.set_trace()
for car in cars:
    print(car)
# pdb.set_trace()
# print(cars[9])

def add(v1,v2):    
    print(v1+v2)
breakpoint()
add("hello",78)