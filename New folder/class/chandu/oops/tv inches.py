class Tv:
    inches=32

tv_obj1=Tv()
tv_obj2=Tv()
print(Tv.inches)
print(tv_obj1.inches)
print(tv_obj2.inches)
tv_obj1.inches=72
print(tv_obj1.inches)
print(tv_obj2.inches)
print(Tv.inches)
tv_obj2.inches=90
print(tv_obj1.inches)
print(tv_obj2.inches)
print(Tv.inches)
Tv.inches=100
print(tv_obj1.inches)
print(tv_obj2.inches)
print(Tv.inches)
