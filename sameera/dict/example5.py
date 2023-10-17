#Rename key of a dictionary

sample_dict={
    "name":"kelly",
    "age":25,
    "salary":8000,
    "city":"newyork"
    }


sample_dict['wages']=sample_dict.pop('salary')
print(sample_dict)
