import mlab
from bike import Bike

mlab.connect()

f= Bike(model="honda blade",daily_fee="32000000",image="https://auto.ndtvimg.com/bike-images/medium/honda/x-blade/honda-x-blade.jpg?v=12",year="2018")
f.save()

# 2.read
# 2.1 get cursor
f_objects = Bike.objects() # lazy loading # same as list

