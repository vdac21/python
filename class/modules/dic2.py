# Get all id from the data
data = [{
            "id": 7,
            "email": "michael.lawson@reqres.in",
            "first_name": "Michael",
            "last_name": "Lawson",
            "avatar": "https://reqres.in/img/faces/7-image.jpg"
        },
        {
            "id": 8,
            "email": "lindsay.ferguson@reqres.in",
            "first_name": "Lindsay",
            "last_name": "Ferguson",
            "avatar": "https://reqres.in/img/faces/8-image.jpg"
        }
     ]

#id1 = data[0]["id"]
#id2 = data[1]["id"]

#print(id1, id2)
ids = []
for d in data:
    ids.append(d["id"])
print(ids)






