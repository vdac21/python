# Get the mail and id from the below data

user_info = [{
            "id": 7,
            "email": "michael.lawson@reqres.in",
            "first_name": "Michael",
            "last_name": "Lawson",
            "avatar": "https://reqres.in/img/faces/7-image.jpg"
}]


user_mail = user_info[0]["email"]

user_id = user_info[0]["id"]


print(f"User Mail : {user_mail} and ID : {user_id}")
